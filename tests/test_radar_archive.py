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
