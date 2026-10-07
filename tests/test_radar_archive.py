import json
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from render_radar_archive import render, summary_paragraphs

class ArchiveTests(unittest.TestCase):
    def test_note_limitations_replace_placeholder_and_survive_rebuild(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'radar').mkdir(); (root/'wiki').mkdir()
            note = root/'wiki/paper.md'
            note.write_text("---\narxiv_id: '2609.26292'\n---\n## 局限性\n\n模型解读：仅仿真，p.6。\n\n## 方法\n正文")
            rows = [{'arxiv_id': '2609.26292', 'summary': '历史描述。局限：未核对。实际阅读范围：历史摘要。', 'raw': [], 'wiki': ['wiki/paper.md'], 'reports': []}]
            coverage = root/'radar/archive-coverage.json'
            coverage.write_text(json.dumps({'papers': rows}))
            render(root)
            text = (root/'wiki/radar-archive.md').read_text()
            self.assertIn('模型解读：仅仿真，p.6。', text)
            self.assertNotIn('局限：</strong>未核对', text)
            self.assertIn('实际阅读范围：</strong>历史摘要。', text)
            self.assertEqual(json.loads(coverage.read_text())['papers'], rows)
            note.write_text(note.read_text().replace('仅仿真，p.6。', '新增证据，p.8。'))
            render(root)
            self.assertIn('新增证据，p.8。', (root/'wiki/radar-archive.md').read_text())

    def test_summary_fields_are_separate_paragraphs_and_escaped(self):
        text = summary_paragraphs('历史条目。问题/方法/证据：方法 <script>。为什么重要：意义。局限：未核验。实际阅读范围：摘要。')
        for label in ['问题/方法/证据', '为什么重要', '局限', '实际阅读范围']:
            self.assertIn('<p><strong>' + label + '：</strong>', text)
        self.assertIn('&lt;script&gt;', text)
        self.assertNotIn('<script>', text)
        combined = summary_paragraphs('问题/方法/证据/局限：完整内容。实际阅读范围：摘要。')
        self.assertIn('<strong>问题/方法/证据/局限：</strong>完整内容。', combined)

    def test_unverified_history_and_source_links_render_without_html_injection(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);(root/'radar').mkdir();(root/'wiki').mkdir()
            rows=[{'arxiv_id':'2506.09985','summary':'<script>alert(1)</script>', 'raw':['raw/World-Models/paper.fulltext.md'],'reports':['radar/reports/weekly/report.md']}]
            (root/'radar/archive-coverage.json').write_text(json.dumps({'papers':rows}))
            self.assertEqual(render(root),1)
            text=(root/'wiki/radar-archive.md').read_text()
            self.assertNotIn('<script>',text)
            self.assertIn('&lt;script&gt;',text)
            self.assertIn('尚未人工核验',text)
            self.assertIn('历史扫描时间',text)
            self.assertIn('/blob/main/raw/World-Models/paper.fulltext.md',text)
            self.assertIn('/blob/main/radar/reports/weekly/report.md',text)

    def test_grouping_official_titles_order_and_withdrawn_state(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);(root/'radar').mkdir();(root/'wiki').mkdir()
            rows=[{'arxiv_id':ident,'summary':summary,'raw':['raw/Deep-Learning/'+ident+'.fulltext.md'],'reports':['radar/reports/weekly/W17.md'],'wiki':[]}
                  for ident,summary in [('2601.10999','已撤回'),('2605.20811','历史摘要')]]
            (root/'radar/archive-coverage.json').write_text(json.dumps({'papers':rows}))
            (root/'radar/catalog.json').write_text(json.dumps({'papers':[
                {'arxiv_id':r['arxiv_id'],'title':'Official '+r['arxiv_id'],'tags':['physics-informed-ai']} for r in rows]}))
            render(root)
            text=(root/'wiki/radar-archive.md').read_text()
            self.assertIn('世界模型与物理建模 · 2 篇',text)
            self.assertNotIn('topic-deep-learning',text)
            self.assertEqual(text.count('<summary><strong>Official'),2)
            self.assertLess(text.index('Official 2605.20811'),text.index('Official 2601.10999'))
            self.assertIn('已撤回 · 仅供历史参考',text)
            self.assertIn('按周查看原始扫描报告',text)
