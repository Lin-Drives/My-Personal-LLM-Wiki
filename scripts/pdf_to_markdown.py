"""Extract page text into raw Markdown; no model rewriting or OCR."""
import argparse
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def convert(job):
    identity, relative_pdf = job
    import pypdf
    source = ROOT / relative_pdf
    # Keep published source links stable when the local PDF gains a title.
    destination = (source.parent / (identity + '.fulltext.md')
                   if source.stem.endswith('arxiv-' + identity)
                   else source.with_suffix('.fulltext.md'))
    if destination.exists():
        return {'arxiv_id': identity, 'status': 'skipped', 'markdown': destination.relative_to(ROOT).as_posix()}
    try:
        reader = pypdf.PdfReader(source)
        pages, empty, repaired = [], [], []
        for number, page in enumerate(reader.pages, 1):
            text = page.extract_text() or ''
            if any(0xD800 <= ord(c) <= 0xDFFF for c in text):
                text = text.encode('utf-16', errors='surrogatepass').decode('utf-16', errors='replace')
                repaired.append(number)
            if not text.strip(): empty.append(number)
            fence = '`' * max(3, max((len(s) + 1 for s in __import__('re').findall(r'`+', text)), default=3))
            pages.append(f'## PDF page {number}\n\n{fence}text\n{text.rstrip()}\n{fence}\n')
        if len(empty) == len(pages): raise ValueError('No extractable text; OCR required')
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        converted_at = datetime.now(timezone.utc).isoformat()
        header = [f'# arXiv:{identity} — PDF 原文文本提取', '', f'- Source: https://arxiv.org/abs/{identity}', f'- Local PDF: `{source.name}` (local only)', f'- PDF SHA-256: `{digest}`', f'- Converted at: {converted_at}', f'- Extractor: pypdf/{pypdf.__version__}', f'- Pages: {len(pages)}', f'- Pages without extractable text: {empty or "none"}', f'- Pages with Unicode surrogate repair: {repaired or "none"} (unpaired values replaced)', '', '> 逐页提取 PDF 文本，未使用模型改写或翻译，未进行内容核验。保留页码；多栏阅读顺序、公式、表格和图片可能不能准确还原。无文字页需要另行 OCR，不能视为完整文本覆盖。基础 ID 的具体版本尚未解析，以 PDF 哈希标识本次原文件。', '']
        temporary = destination.with_suffix('.md.tmp')
        temporary.write_text('\n'.join(header) + '\n' + '\n'.join(pages), encoding='utf-8')
        temporary.replace(destination)
        return {'arxiv_id': identity, 'status': 'converted', 'pdf': relative_pdf, 'markdown': destination.relative_to(ROOT).as_posix(), 'pdf_sha256': digest, 'pages': len(pages), 'empty_pages': empty, 'unicode_repaired_pages': repaired, 'converted_at': converted_at}
    except Exception as error:
        return {'arxiv_id': identity, 'status': 'failed', 'pdf': relative_pdf, 'error': str(error)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workers', type=int, default=4)
    args = parser.parse_args()
    if not 1 <= args.workers <= 4: parser.error('workers must be 1..4')
    manifest = json.loads((ROOT / 'radar/download-manifest.json').read_text())
    jobs = [(identity, str((ROOT / row['path']).resolve().relative_to(ROOT))) for identity, row in manifest['papers'].items() if row['status'] in ('downloaded', 'skipped')]
    result_path = ROOT / 'radar/pdf-conversion-manifest.json'
    prior = {r['arxiv_id']: r for r in json.loads(result_path.read_text())['papers']} if result_path.exists() else {}
    results = []
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        for result in pool.map(convert, jobs):
            results.append(prior.get(result['arxiv_id'], result) if result['status'] == 'skipped' else result)
            print(result['arxiv_id'] + ': ' + result['status'], flush=True)
    (ROOT / 'radar/pdf-conversion-manifest.json').write_text(json.dumps({'papers': results}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({s: sum(r['status'] == s for r in results) for s in ('converted', 'skipped', 'failed')}))
    return 2 if any(r['status'] == 'failed' for r in results) else 0


if __name__ == '__main__':
    raise SystemExit(main())
