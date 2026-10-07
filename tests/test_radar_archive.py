import json
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from render_radar_archive import render

class ArchiveTests(unittest.TestCase):
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
