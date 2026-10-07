"""Publish a historical reading inventory; archived interpretations remain unverified."""
import html
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GITHUB = 'https://github.com/Lin-Drives/My-Personal-LLM-Wiki/blob/main/'


def render(root=ROOT):
    rows = json.loads((root / 'radar/archive-coverage.json').read_text(encoding='utf-8'))['papers']
    catalog_path = root / 'radar/catalog.json'
    catalog = {}
    if catalog_path.exists():
        for paper in json.loads(catalog_path.read_text(encoding='utf-8'))['papers']:
            catalog[paper['arxiv_id']] = paper
    topics = [('World-Models', '世界模型与物理建模'), ('Embodied-Intelligence', '具身智能'),
              ('Deep-Learning', '深度学习'), ('AI-Infra', 'AI 基础设施'),
              ('Chip-Architecture', 'AI 芯片架构'), ('Reinforcement-Learning', '强化学习'),
              ('Other', '其他与待确认来源')]
    grouped = defaultdict(list)
    for row in rows:
        paper = catalog.get(row['arxiv_id'], {})
        tags = paper.get('tags', [])
        category = next((key for key, _ in topics if any('/' + key + '/' in path
                        for path in row.get('raw', []) + row.get('wiki', []))), 'Other')
        if 'embodied-intelligence' in tags:
            category = 'Embodied-Intelligence'
        elif any(tag in tags for tag in ('world-models', 'physics-informed-ai')):
            category = 'World-Models'
        grouped[category].append(row)
    safe = lambda text: html.escape(str(text), quote=True)
    lines = ['---','type: Research Feed','title: 历史论文雷达与原文库','description: 保存历史雷达筛选线索及已提取的论文原文入口。','tags: [论文雷达, 原文库]','status: draft','sources:','  - id: archive-coverage','    resource: ../radar/archive-coverage.json','---','','# 历史论文雷达与原文库','','> 历史扫描与工具解读，尚未人工核验。被雷达推荐代表当时的选题判断，不等于重要性或论文结论已被确认。原文是 PDF 文本提取，公式、表格和图片可能缺失。','','历史扫描时间来自报告文件修改时间，属于估计，不作为实际发现时间。论文发表日期以 arXiv 页面为准。原文与周报链接在 GitHub 打开；PDF 仅保留本地。','',f'按基础 arXiv ID 汇总 {len(rows)} 篇，重复出现的论文保留所有周报来源。','']
    lines += ['## 按主题浏览', '', '每篇仅在一个主题出现；主题内按 arXiv ID 从新到旧排列。点击标题行展开历史解读与来源。', '']
    for key, label in topics:
        if grouped[key]:
            lines += [f'- [{label} · {len(grouped[key])} 篇](#topic-{key.lower()})']
    reports = sorted({path for row in rows for path in row['reports']}, reverse=True)
    lines += ['', '<details><summary>按周查看原始扫描报告</summary>', '<ul>']
    lines += [f'<li><a href="{GITHUB+safe(path)}">{safe(Path(path).stem)}</a></li>' for path in reports]
    lines += ['</ul></details>', '']
    links = lambda paths: ' · '.join(f'<a href="{GITHUB+safe(path)}">{safe(Path(path).name)}</a>' for path in paths)
    for key, label in topics:
        if not grouped[key]:
            continue
        lines += [f'<h2 id="topic-{key.lower()}">{safe(label)} · {len(grouped[key])} 篇</h2>', '']
        for row in sorted(grouped[key], key=lambda item: item['arxiv_id'], reverse=True):
            fulltext = [p for p in row['raw'] if p.endswith('.fulltext.md')]
            paper = catalog.get(row['arxiv_id'], {})
            title = paper.get('title', '来源待确认（请查看历史报告）')
            state = '已有知识笔记' if row.get('wiki') else ('原文可读' if fulltext else '原文待补')
            if '撤回' in row['summary'] or 'withdrawn' in row['summary'].lower():
                state = '已撤回 · 仅供历史参考'
            lines += ['<details>', f'<summary><strong>{safe(title)}</strong><br><small>arXiv:{safe(row["arxiv_id"])} · {safe(state)}</small></summary>',
                      f'<p><a href="https://arxiv.org/abs/{safe(row["arxiv_id"])}">arXiv 页面</a></p>',
                      f'<p><strong>历史扫描解读：</strong>{safe(row["summary"])}</p>',
                      '<p><strong>原文：</strong>' + (links(fulltext) or '尚未取得可用原文；来源异常及撤回说明见历史解读。') + '</p>']
            if row.get('wiki'):
                wiki_links = ' · '.join(f'<a href="../{safe(path.removeprefix("wiki/").removesuffix(".md"))}/">{safe(Path(path).stem)}</a>' for path in row['wiki'])
                lines += ['<p><strong>知识笔记：</strong>' + wiki_links + '</p>']
            lines += ['<p><strong>扫描来源：</strong>' + links(row['reports']) + '</p>', '</details>', '']
    target=root/'wiki/radar-archive.md'
    target.write_text('\n'.join(lines),encoding='utf-8')
    return len(rows)


if __name__ == '__main__':
    print('Archived papers:',render())
