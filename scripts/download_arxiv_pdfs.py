"""Download arXiv PDFs from IDs or radar JSON; serial, throttled, restartable."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import time
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parent.parent
TOPICS = {'ai-infra': 'AI-Infra', 'deep-learning': 'Deep-Learning', 'physics-informed-ai': 'Deep-Learning', 'world-models': 'World-Models', 'embodied-intelligence': 'Embodied-Intelligence'}


def topic_for(row):
    for path in row.get('wiki', []) + row.get('raw', []):
        parts = Path(path).parts
        if len(parts) > 2 and parts[1] in set(TOPICS.values()) | {'Chip-Architecture', 'Companies', 'Reinforcement-Learning'}:
            return parts[1]
    for report in row.get('reports', []):
        for slug, topic in TOPICS.items():
            if slug in Path(report).stem: return topic
        if Path(report).stem == '2026-W17': return 'World-Models'
    for tag in row.get('tags', []):
        if tag.lower() in TOPICS: return TOPICS[tag.lower()]
    return None


PATTERN = re.compile(r'\d{4}\.\d{4,5}(?:v[1-9]\d*)?')


def valid_pdf(path):
    if not path.is_file() or path.stat().st_size < 20:
        return False
    with path.open('rb') as f:
        if f.read(5) != b'%PDF-': return False
        f.seek(max(0, path.stat().st_size - 2048))
        return b'%%EOF' in f.read()


def identities(data):
    rows = data['papers']
    result = []
    for row in rows:
        value = row['arxiv_id'] + row.get('arxiv_version', '')
        if not PATTERN.fullmatch(value): raise ValueError('Invalid arXiv ID: ' + value)
        result.append(value)
    return list(dict.fromkeys(result))


class Downloader:
    def __init__(self, interval=3, attempts=3, opener=urllib.request.urlopen):
        self.interval, self.attempts, self.opener = interval, attempts, opener
        self.last_request = 0

    def download(self, identity, directory):
        if not PATTERN.fullmatch(identity): raise ValueError('Invalid arXiv ID')
        directory.mkdir(parents=True, exist_ok=True)
        target = directory / (identity + '.pdf')
        if valid_pdf(target): return {'arxiv_id': identity, 'status': 'skipped', 'path': str(target)}
        # Preserve an existing corrupt file for inspection rather than overwriting it.
        if target.exists(): return {'arxiv_id': identity, 'status': 'failed', 'error': 'Existing PDF is incomplete; move it aside before retrying', 'path': str(target)}
        temporary = directory / (identity + '.pdf.part')
        url = 'https://arxiv.org/pdf/' + identity
        error = ''
        for attempt in range(self.attempts):
            time.sleep(max(0, self.interval - (time.monotonic() - self.last_request)))
            self.last_request = time.monotonic()
            try:
                request = urllib.request.Request(url, headers={'User-Agent': 'PersonalLLMWiki/1.0 (paper archival)'})
                with self.opener(request, timeout=90) as response, temporary.open('wb') as out:
                    total = 0
                    expected = response.headers.get('Content-Length')
                    while True:
                        chunk = response.read(256 * 1024)
                        if not chunk: break
                        out.write(chunk); total += len(chunk)
                    if expected and total != int(expected): raise ValueError('Incomplete response')
                if not valid_pdf(temporary): raise ValueError('Response is not a complete PDF')
                temporary.replace(target)
                digest = hashlib.sha256()
                with target.open('rb') as source:
                    for chunk in iter(lambda: source.read(256 * 1024), b''): digest.update(chunk)
                return {'arxiv_id': identity, 'status': 'downloaded', 'path': str(target), 'url': url, 'sha256': digest.hexdigest(), 'downloaded_at': datetime.now(timezone.utc).isoformat(), 'version': 'explicit' if 'v' in identity else 'unresolved latest at download time'}
            except (OSError, ValueError) as exc:
                error = str(exc)
                temporary.unlink(missing_ok=True)
                if isinstance(exc, urllib.error.HTTPError) and exc.code in (400, 404, 410): break
                if attempt + 1 < self.attempts:
                    delay = min(60, 3 * 2 ** attempt)
                    if isinstance(exc, urllib.error.HTTPError):
                        retry = exc.headers.get('Retry-After', '')
                        if retry.isdigit(): delay = max(delay, int(retry))
                    time.sleep(delay)
        return {'arxiv_id': identity, 'status': 'failed', 'url': url, 'error': error}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('ids', nargs='*')
    parser.add_argument('--input', type=Path, help='Scan JSON or archive-coverage.json')
    parser.add_argument('--output', type=Path, help='Optional explicit output directory; otherwise use raw/<topic>')
    parser.add_argument('--limit', type=int, help='Process only first N unique IDs')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding='utf-8')) if args.input else {'papers': []}
    ids = args.ids + identities(data)
    topics = {row['arxiv_id'] + row.get('arxiv_version', ''): topic_for(row) for row in data['papers']}
    if args.output is None and any(not topics.get(i) for i in ids):
        parser.error('Classification missing; use coverage JSON or an explicit --output raw/<topic>')
    destinations = {i: args.output or ROOT / 'raw' / topics[i] for i in ids}
    ids = list(dict.fromkeys(ids))
    if not ids or any(not PATTERN.fullmatch(i) for i in ids): parser.error('Supply valid modern arXiv IDs or --input')
    if args.limit is not None:
        if args.limit < 1: parser.error('--limit must be positive')
        ids = ids[:args.limit]
    # Skip existing canonical filenames across legacy topic directories too.
    existing = {}
    for p in (ROOT / 'raw').rglob('*.pdf'):
        matches = PATTERN.findall(p.stem)
        if len(matches) == 1 and valid_pdf(p): existing.setdefault(matches[0], p)
    if args.dry_run:
        print(json.dumps({'unique_ids': len(ids), 'existing_named_pdfs': sum(i in existing or valid_pdf(destinations[i] / (i + '.pdf')) for i in ids), 'topics': {t: sum(topics.get(i) == t for i in ids) for t in sorted(set(topics.values()) - {None})}}, ensure_ascii=False)); return 0
    downloader = Downloader()
    results = []
    manifest = ROOT / 'radar/download-manifest.json'
    manifest.parent.mkdir(parents=True, exist_ok=True)
    prior = json.loads(manifest.read_text()) if manifest.exists() else {'papers': {}}
    for identity in ids:
        result = {'arxiv_id': identity, 'status': 'skipped', 'path': str(existing[identity])} if identity in existing else downloader.download(identity, destinations[identity])
        results.append(result)
        # Preserve original download provenance when reruns skip a successful file.
        if result['status'] != 'skipped' or identity not in prior['papers']: prior['papers'][identity] = result
        temporary = manifest.with_suffix('.json.tmp')
        temporary.write_text(json.dumps(prior, ensure_ascii=False, indent=2) + '\n'); temporary.replace(manifest)
        print(identity + ': ' + result['status'], flush=True)
    print(json.dumps({s: sum(r['status'] == s for r in results) for s in ('downloaded', 'skipped', 'failed')}))
    return 2 if any(r['status'] == 'failed' for r in results) else 0


if __name__ == '__main__':
    raise SystemExit(main())
