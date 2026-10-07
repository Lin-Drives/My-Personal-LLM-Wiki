import json
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from rename_local_pdfs import rename


class NamingTests(unittest.TestCase):
    def test_arxiv_prefix_and_previous_rename_history(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'radar').mkdir(); (root/'raw').mkdir()
            (root/'radar/catalog.json').write_text(json.dumps({'papers': [{'arxiv_id': '2605.24934', 'published_at': '2026-05-28T00:00:00Z', 'title': 'HumanEgo'}]}))
            (root/'raw/arxiv-2605.24934.pdf').write_bytes(b'PDF bytes')
            old_history = {'old': 'previous.pdf', 'new': 'renamed.pdf', 'sha256': 'history'}
            (root/'radar/pdf-renaming-report.json').write_text(json.dumps({'renamed': [old_history]}))
            result = rename(root, apply=True)
            self.assertEqual(result['renamed'], 1)
            self.assertEqual((root/'raw/2026-05-28-humanego-arxiv-2605.24934.pdf').read_bytes(), b'PDF bytes')
            report = json.loads((root/'radar/pdf-renaming-report.json').read_text())
            self.assertEqual(report['renamed'][0], old_history)
            self.assertEqual(len(report['renamed']), 2)

    def test_rename_preserves_bytes_updates_reference_and_skips_unknown(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'radar').mkdir(); (root/'raw').mkdir()
            (root/'radar/catalog.json').write_text(json.dumps({'papers': [{'arxiv_id': '2605.24934', 'published_at': '2026-05-28T00:00:00Z', 'title': 'HumanEgo'}]}))
            (root/'raw/2605.24934.pdf').write_bytes(b'unchanged PDF bytes')
            (root/'raw/2605.0645.pdf').write_bytes(b'unknown identity')
            md = root/'raw/2605.24934.fulltext.md'
            md.write_bytes(b'- Local PDF: `2605.24934.pdf`\nText\r\rformula')
            self.assertEqual(rename(root)['planned'], 1)
            self.assertTrue((root/'raw/2605.24934.pdf').exists())
            result = rename(root, apply=True)
            self.assertEqual(result['renamed'], 1)
            name = '2026-05-28-humanego-arxiv-2605.24934.pdf'
            self.assertEqual((root/'raw'/name).read_bytes(), b'unchanged PDF bytes')
            self.assertIn(b'Text\r\rformula', md.read_bytes())
            self.assertIn(name.encode(), md.read_bytes())
            self.assertTrue((root/'raw/2605.0645.pdf').exists())
            self.assertEqual(rename(root)['planned'], 0)
