"""Rename ID-only local PDFs using confirmed catalog dates and titles."""
import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent


def filename(paper, identity):
    date = paper['published_at'][:10]
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', date):
        raise ValueError('Missing publication date')
    slug = re.sub(r'[^a-z0-9]+', '-', paper['title'].lower()).strip('-')[:110].rstrip('-')
    if not slug:
        raise ValueError('Missing title slug')
    return f'{date}-{slug}-arxiv-{identity}.pdf'


def rename(root=ROOT, apply=False):
    catalog = {p['arxiv_id']: p for p in json.loads((root/'radar/catalog.json').read_text())['papers']}
    changes, skipped = [], []
    for source in sorted((root/'raw').rglob('*.pdf')):
        if not re.fullmatch(r'\d{4}\.\d{4,5}(?:v\d+)?', source.stem):
            continue
        identity = re.sub(r'v\d+$', '', source.stem)
        paper = catalog.get(identity)
        if not paper:
            skipped.append({'path': str(source.relative_to(root)), 'reason': 'No confirmed catalog identity'})
            continue
        target = source.with_name(filename(paper, source.stem))
        if target.exists():
            raise ValueError('Target already exists: ' + str(target))
        changes.append({'old': str(source.relative_to(root)), 'new': str(target.relative_to(root)),
                        'sha256': hashlib.sha256(source.read_bytes()).hexdigest()})
    if apply:
        for row in changes:
            (root/row['old']).rename(root/row['new'])
            if hashlib.sha256((root/row['new']).read_bytes()).hexdigest() != row['sha256']:
                raise ValueError('PDF hash changed')
        # Update path references, never the extracted paper text or source hashes.
        mapping = {row['old']: row['new'] for row in changes}
        def replace(value):
            if isinstance(value, dict): return {k: replace(v) for k, v in value.items()}
            if isinstance(value, list): return [replace(v) for v in value]
            if isinstance(value, str):
                for old, new in mapping.items():
                    if value == old or value == str(root/old):
                        return new if value == old else str(root/new)
            return value
        for name in ['download-manifest.json', 'pdf-conversion-manifest.json', 'archive-coverage.json']:
            path = root/'radar'/name
            if path.exists():
                data = json.loads(path.read_text())
                updated = replace(data)
                if updated != data: path.write_text(json.dumps(updated, ensure_ascii=False, indent=2)+'\n')
        for row in changes:
            source = root/row['old']
            md = source.with_suffix('.fulltext.md')
            if md.exists():
                text = md.read_bytes().decode('utf-8')
                text = text.replace(f'- Local PDF: `{source.name}`', f'- Local PDF: `{Path(row["new"]).name}`', 1)
                md.write_bytes(text.encode('utf-8'))
        (root/'radar/pdf-renaming-report.json').write_text(json.dumps({'naming': 'publication-date-title-arxiv-id; authors omitted; descriptive legacy names preserved', 'renamed': changes, 'skipped': skipped}, ensure_ascii=False, indent=2)+'\n')
    return {'renamed' if apply else 'planned': len(changes), 'skipped': skipped}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    print(json.dumps(rename(apply=parser.parse_args().apply), ensure_ascii=False, indent=2))
