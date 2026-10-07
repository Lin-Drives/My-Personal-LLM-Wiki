"""Publish a historical reading inventory; archived interpretations remain unverified."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GITHUB = 'https://github.com/Lin-Drives/My-Personal-LLM-Wiki/blob/main/'


def render(root=ROOT):
    rows = json.loads((root / 'radar/archive-coverage.json').read_text(encoding='utf-8'))['papers']
    safe = lambda text: html.escape(str(text), quote=True)
    lines = ['---','type: Research Feed','title: 历史论文雷达与原文库','description: 保存历史雷达筛选线索及已提取的论文原文入口。','tags: [论文雷达, 原文库]','status: draft','sources:','  - id: archive-coverage','    resource: ../radar/archive-coverage.json','---','','# 历史论文雷达与原文库','','> 历史扫描与工具解读，尚未人工核验。被雷达推荐代表当时的选题判断，不等于重要性或论文结论已被确认。原文是 PDF 文本提取，公式、表格和图片可能缺失。','','历史扫描时间来自报告文件修改时间，属于估计，不作为实际发现时间。论文发表日期以 arXiv 页面为准。原文与周报链接在 GitHub 打开；PDF 仅保留本地。','',f'按基础 arXiv ID 汇总 {len(rows)} 篇，重复出现的论文保留所有周报来源。','']
    for row in rows:
        fulltext=[p for p in row['raw'] if p.endswith('.fulltext.md')]
        lines += ['<article>',f'<h2><a href="https://arxiv.org/abs/{safe(row["arxiv_id"])}">arXiv:{safe(row["arxiv_id"])}</a></h2>',f'<p><strong>历史扫描解读：</strong>{safe(row["summary"])}</p>']
        links = lambda paths: ' · '.join(f'<a href="{GITHUB+safe(path)}">{safe(Path(path).name)}</a>' for path in paths)
        lines += ['<p><strong>原文：</strong>'+ (links(fulltext) or '尚未取得可提取的原文，见下载失败清单。')+'</p>', '<p><strong>扫描来源：</strong>'+links(row['reports'])+'</p>','</article>','']
    target=root/'wiki/radar-archive.md'
    target.write_text('\n'.join(lines),encoding='utf-8')
    return len(rows)


if __name__ == '__main__':
    print('Archived papers:',render())
