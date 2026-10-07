import json
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from rename_local_pdfs import rename


class NamingTests(unittest.TestCase):
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
