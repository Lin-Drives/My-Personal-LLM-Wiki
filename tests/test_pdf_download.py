import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from download_arxiv_pdfs import Downloader, identities, valid_pdf, topic_for

PDF = b'%PDF-1.7\n' + b'fixture\n' * 10 + b'%%EOF\n'

class Response(io.BytesIO):
    def __init__(self, data):
        super().__init__(data)
        self.headers = {'Content-Length': str(len(data))}

class PDFTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def test_download_and_skip(self):
        calls=[]
        def opener(*args, **kwargs): calls.append(args); return Response(PDF)
        d=Downloader(interval=0, opener=opener)
        self.assertEqual(d.download('2506.09985v1',self.root)['status'],'downloaded')
        self.assertTrue(valid_pdf(self.root/'2506.09985v1.pdf'))
        self.assertEqual(d.download('2506.09985v1',self.root)['status'],'skipped')
        self.assertEqual(len(calls),1)

    def test_html_is_rejected_without_final_file(self):
        d=Downloader(interval=0,attempts=1,opener=lambda *a,**k:Response(b'<html>Error</html>'))
        self.assertEqual(d.download('2506.09985',self.root)['status'],'failed')
        self.assertFalse(list(self.root.iterdir()))

    def test_retry_and_existing_corrupt_file_preserved(self):
        responses=[OSError('temporary'),Response(PDF)]
        def opener(*a,**k):
            value=responses.pop(0)
            if isinstance(value,Exception): raise value
            return value
        with patch('download_arxiv_pdfs.time.sleep'):
            self.assertEqual(Downloader(interval=0,opener=opener).download('2506.09985',self.root)['status'],'downloaded')
        (self.root/'2506.00001.pdf').write_bytes(b'corrupt')
        self.assertEqual(Downloader(interval=0).download('2506.00001',self.root)['status'],'failed')
        self.assertEqual((self.root/'2506.00001.pdf').read_bytes(),b'corrupt')

    def test_dedup_and_bad_identity(self):
        self.assertEqual(identities({'papers':[{'arxiv_id':'2506.09985'}]*2}),['2506.09985'])
        with self.assertRaises(ValueError): identities({'papers':[{'arxiv_id':'../escape'}]})

    def test_topic_follows_existing_material_then_report(self):
        self.assertEqual(topic_for({"wiki": ["wiki/World-Models/paper.md"], "reports": ["radar/paperradar/weekly/2026-W41-embodied-intelligence.md"]}), "World-Models")
        self.assertEqual(topic_for({"reports": ["radar/paperradar/weekly/2026-W39-physics-informed-ai.md"]}), "Deep-Learning")
        self.assertIsNone(topic_for({}))
