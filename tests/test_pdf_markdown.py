from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import pdf_to_markdown

class ConversionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root/'raw').mkdir()
        (self.root/'raw/paper.pdf').write_bytes(b'fixture')

    def run_conversion(self, texts):
        fake = SimpleNamespace(__version__='test', PdfReader=lambda _: SimpleNamespace(pages=[SimpleNamespace(extract_text=lambda value=value: value) for value in texts]))
        with patch.object(pdf_to_markdown,'ROOT',self.root), patch.dict(sys.modules,{'pypdf':fake}):
            return pdf_to_markdown.convert(('2506.09985','raw/paper.pdf'))

    def test_page_text_provenance_and_no_overwrite(self):
        r=self.run_conversion(['Original evidence', 'Formula ``` example'])
        self.assertEqual(r['status'],'converted')
        text=(self.root/'raw/paper.fulltext.md').read_text()
        self.assertIn('PDF page 2',text);self.assertIn('Original evidence',text);self.assertIn('PDF SHA-256',text)
        self.assertEqual(self.run_conversion(['changed'])['status'],'skipped')
        self.assertEqual((self.root/'raw/paper.fulltext.md').read_text(),text)

    def test_no_text_fails_without_markdown(self):
        self.assertEqual(self.run_conversion([''])['status'],'failed')
        self.assertFalse((self.root/'raw/paper.fulltext.md').exists())

    def test_surrogate_pair_normalized(self):
        r=self.run_conversion(['Math \ud835\udc00'])
        self.assertEqual(r['status'],'converted')
        self.assertEqual(r['unicode_repaired_pages'],[1])
        self.assertIn('Math 𝐀',(self.root/'raw/paper.fulltext.md').read_text())
