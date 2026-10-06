"""Validate project OKF v0.2 metadata; this is not factual verification."""
from pathlib import Path
import re
from urllib.parse import urlparse
import yaml

ROOT = Path(__file__).resolve().parent.parent


def frontmatter(text):
    match = re.match(r'\A---\n(.*?)\n---(?:\n|$)', text, re.S)
    if not match:
        return None
    result = yaml.safe_load(match[1])
    if not isinstance(result, dict):
        raise ValueError('frontmatter must be a mapping')
    return result


def validate(wiki_dir):
    count = 0
    for path in sorted(wiki_dir.rglob('*.md')):
        meta = frontmatter(path.read_text(encoding='utf-8'))
        if path.name in ('index.md', 'log.md'):
            expected = {'okf_version': '0.2'} if path == wiki_dir / 'index.md' else None
            if meta != expected:
                raise ValueError(str(path) + ': invalid index/log metadata')
            continue
        if not meta:
            raise ValueError(str(path) + ': missing OKF frontmatter')
        for key in ('type', 'title', 'description'):
            if not isinstance(meta.get(key), str) or not meta[key].strip():
                raise ValueError(str(path) + ': missing ' + key)
        if not isinstance(meta.get('tags'), list) or not all(isinstance(t, str) for t in meta['tags']):
            raise ValueError(str(path) + ': invalid tags')
        if meta.get('status') not in ('draft', 'stable', 'deprecated'):
            raise ValueError(str(path) + ': invalid status')
        ids = set()
        sources = meta.get('sources', [])
        if not isinstance(sources, list):
            raise ValueError(str(path) + ': sources must be a list')
        for source in sources:
            if not isinstance(source, dict):
                raise ValueError(str(path) + ': invalid source')
            identity, resource = source.get('id'), source.get('resource')
            if not isinstance(identity, str) or not identity or identity in ids:
                raise ValueError(str(path) + ': missing/duplicate source id')
            ids.add(identity)
            if not isinstance(resource, str) or not resource:
                raise ValueError(str(path) + ': missing source resource')
            uri = urlparse(resource)
            if uri.scheme:
                if uri.scheme not in ('https', 'http') or not uri.netloc:
                    raise ValueError(str(path) + ': invalid source URL')
            else:
                target = wiki_dir / resource.lstrip('/') if resource.startswith('/') else path.parent / resource
                if not target.is_file():
                    raise ValueError(str(path) + ': missing source file ' + resource)
        arxiv_id = meta.get('arxiv_id')
        if arxiv_id is not None:
            if not isinstance(arxiv_id, str) or not re.fullmatch(r'\d{4}\.\d{4,5}', arxiv_id):
                raise ValueError(str(path) + ': invalid arxiv_id')
            version = meta.get('arxiv_version', '')
            if version and not re.fullmatch(r'v[1-9]\d*', str(version)):
                raise ValueError(str(path) + ': invalid arxiv_version')
            if meta.get('resource') != 'https://arxiv.org/abs/' + arxiv_id + version:
                raise ValueError(str(path) + ': arXiv resource mismatch')
        count += 1
    return count


if __name__ == '__main__':
    print('OKF pages:', validate(ROOT / 'wiki'))
