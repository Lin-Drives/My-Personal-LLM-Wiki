from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from validate_okf import validate


class OKFTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.wiki = Path(self.temp.name)
        (self.wiki / 'index.md').write_text('---\nokf_version: "0.2"\n---\n# Index\n')
        self.page = self.wiki / 'paper.md'
        self.base = 'type: Paper Note\ntitle: Paper\ndescription: Context\ntags: [robotics]\nstatus: draft\n'

    def page_with(self, metadata):
        self.page.write_text('---\n' + metadata + '---\n# Paper\n')

    def test_valid_page_and_reserved_files(self):
        self.page_with(self.base)
        (self.wiki / 'log.md').write_text('# Log\n')
        sub = self.wiki / 'topic'
        sub.mkdir()
        (sub / 'index.md').write_text('# Topic\n')
        self.assertEqual(validate(self.wiki), 1)

    def test_missing_type_and_extra_index_metadata_fail(self):
        self.page_with(self.base.replace('type: Paper Note\n', ''))
        with self.assertRaises(ValueError): validate(self.wiki)
        self.page_with(self.base)
        (self.wiki / 'index.md').write_text('---\nokf_version: "0.2"\nhide: [toc]\n---\n')
        with self.assertRaises(ValueError): validate(self.wiki)

    def test_missing_source_and_duplicate_id_fail(self):
        self.page_with(self.base + 'sources:\n- id: raw\n  resource: absent.md\n')
        with self.assertRaises(ValueError): validate(self.wiki)
        self.page_with(self.base + 'sources:\n- id: raw\n  resource: paper.md\n- id: raw\n  resource: paper.md\n')
        with self.assertRaises(ValueError): validate(self.wiki)

    def test_arxiv_identity_must_match_resource(self):
        self.page_with(self.base + 'arxiv_id: "2506.09985"\nresource: https://arxiv.org/abs/2506.00001\n')
        with self.assertRaises(ValueError): validate(self.wiki)
