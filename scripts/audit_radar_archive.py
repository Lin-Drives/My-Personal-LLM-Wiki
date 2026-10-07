"""Inventory historical radar papers against local primary materials, without web verification."""
import json
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
ID = re.compile(r'(?<!\d)(\d{4}\.\d{4,5})(?:v[1-9]\d*)?(?!\d)')


def inventory(root):
    raw = defaultdict(set)
    for p in (root / 'raw').rglob('*'):
        if not p.is_file() or p.suffix not in ('.md', '.pdf', '.xml'):
            continue
        # Weekly syntheses are secondary references, not stored primary papers.
        if re.search(r'W\d{2}', p.name):
            continue
        text = p.name
        if p.suffix == '.md':
            text += '\n' + p.read_text(encoding='utf-8')[:2500]
        for identity in ID.findall(text):
            raw[identity].add(p.relative_to(root).as_posix())
    wiki = defaultdict(set)
    mentions = defaultdict(set)
    for p in (root / 'wiki').rglob('*.md'):
        if p.name in ('index.md', 'log.md', 'updates.md', 'overview.md', 'knowledge-graph.md', 'radar-archive.md'):
            continue
        text = p.read_text(encoding='utf-8')
        rel = p.relative_to(root).as_posix()
        # Source declarations before overview/raw content are direct coverage evidence.
        cutoff = re.search(r'^## (?:Overview|原始内容|Raw Content|公司定位)', text, re.M)
        section = text[:cutoff.start()] if cutoff else text.split('\n## ', 1)[0]
        ids = set(ID.findall(section))
        for path in re.findall(r'(?:resource:\s*|\]\()([^\s)]+\.md)', section):
            if 'raw/' not in path:
                continue
            target = 'raw/' + path.split('raw/', 1)[1]
            for identity, files in raw.items():
                if target in files:
                    ids.add(identity)
        for identity in ids:
            wiki[identity].add(rel)
        for identity in set(ID.findall(text)) - ids:
            mentions[identity].add(rel)
    papers = {}
    for p in sorted((root / 'radar/reports/weekly').glob('*.json')):
        batch = json.loads(p.read_text(encoding='utf-8'))
        for item in batch['papers']:
            identity = item['arxiv_id']
            row = papers.setdefault(identity, {'arxiv_id': identity, 'reports': [], 'wiki': sorted(wiki[identity]), 'raw': sorted(raw[identity]), 'wiki_mentions': sorted(mentions[identity]), 'summary': item['summary']})
            row['reports'].append(p.with_suffix('.md').relative_to(root).as_posix())
    for row in papers.values():
        row['status'] = 'wiki' if row['wiki'] else 'raw_only' if row['raw'] else 'radar_only'
    return list(papers.values())


def render(root):
    rows = inventory(root)
    counts = {k: sum(r['status'] == k for r in rows) for k in ('wiki', 'raw_only', 'radar_only')}
    report = {'method': 'Local ID and declared-source matching; no online identity or factual verification. Raw matches are candidates inferred from filenames and the first 2500 characters, not verified full text.', 'counts': counts, 'papers': rows}
    destination = root / 'radar/archive-coverage.json'
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = ['# 历史论文雷达收录核对', '', '按基础 arXiv ID 去重，对照本地知识文章的来源声明和原始材料。未联网核验论文身份或结论；版本未逐一比较。原始材料匹配仅根据文件名与开头 2500 字符，不能保证是完整原文。文章出现 ID 不等于已有深入解读。', '', f"共 {len(rows)} 篇：知识文章来源已关联 {counts['wiki']}；仅有原始材料候选 {counts['raw_only']}；仅在雷达中 {counts['radar_only']}。", '', '历史 JSON 的 scanned_at 沿用报告文件修改时间，只能作为估计；scanned_at_source 明确记录来源，不能作为真实发现时间。', '']
    for status, title in [('radar_only','尚未收录：仅有雷达记录'),('raw_only','已有原始材料候选，尚无知识文章来源关联'),('wiki','已有知识文章来源关联')]:
        lines += ['## '+title, '', '| arXiv ID | 原扫描报告 | 已有材料 / 文章 |', '|---|---|---|']
        for r in rows:
            if r['status'] != status: continue
            links = lambda paths: '、'.join(f'[{Path(p).name}]({"../"+p if not p.startswith("radar/") else p[6:]})' for p in paths)
            existing = links(r['wiki'] + r['raw']) or '未找到'
            if r['wiki_mentions']: existing += '；其他文章仅提及：'+links(r['wiki_mentions'])
            lines.append(f"| [{r['arxiv_id']}](https://arxiv.org/abs/{r['arxiv_id']}) | {links(r['reports'])} | {existing} |")
        lines.append('')
    (root / 'radar/archive-coverage.md').write_text('\n'.join(lines), encoding='utf-8')
    print(counts)


if __name__ == '__main__':
    render(ROOT)
