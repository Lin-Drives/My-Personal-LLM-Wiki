"""Rename ID-only and arxiv-prefixed PDFs using confirmed dates and titles."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from radar_pipeline import source_metadata

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
    for metadata in sorted((root/'raw/arxiv').glob('*.xml')):
        base = re.sub(r'v\d+$', '', metadata.stem)
        if base in catalog:
            continue
        try:
            _, fields = source_metadata(metadata.read_bytes(), base)
            catalog[base] = {'title': fields['title'], 'published_at': fields['published']}
        except (ValueError, ET.ParseError):
            continue
    changes, skipped = [], []
    for source in sorted((root/'raw').rglob('*.pdf')):
        match = re.fullmatch(r'(?:arxiv-)?(\d{4}\.\d{4,5}(?:v\d+)?)', source.stem)
        if not match:
            continue
        file_identity = match.group(1)
        identity = re.sub(r'v\d+$', '', file_identity)
        paper = catalog.get(identity)
        if not paper:
            skipped.append({'path': str(source.relative_to(root)), 'reason': 'No confirmed catalog identity'})
            continue
        target = source.with_name(filename(paper, file_identity))
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
        report_path = root/'radar/pdf-renaming-report.json'
        prior = json.loads(report_path.read_text()) if report_path.exists() else {'renamed': []}
        prior.update({'naming': 'publication-date-title-arxiv-id; authors omitted; descriptive legacy names preserved', 'renamed': prior['renamed'] + changes, 'skipped': skipped})
        report_path.write_text(json.dumps(prior, ensure_ascii=False, indent=2)+'\n')
    return {'renamed' if apply else 'planned': len(changes), 'skipped': skipped}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    print(json.dumps(rename(apply=parser.parse_args().apply), ensure_ascii=False, indent=2))
