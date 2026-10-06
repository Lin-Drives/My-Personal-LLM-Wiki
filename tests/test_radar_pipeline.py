import copy
import hashlib
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from radar_pipeline import ingest, read_json, render, validate, write_json
from research_task import transition


def atom(identity="2601.12345v1", title="Test paper"):
    # Synthetic source fixture; never written into the real catalog or public site.
    return ('<feed xmlns="http://www.w3.org/2005/Atom"><entry>'
            '<id>http://arxiv.org/abs/' + identity + '</id><title>' + title + '</title>'
            '<summary>Original source text.</summary><published>2026-01-01T00:00:00Z</published>'
            '<updated>2026-01-02T00:00:00Z</updated></entry></feed>').encode()


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        write_json(self.root / "radar/catalog.json", {"schema_version": 1, "papers": []})
        self.batch = {"schema_version": 1, "scan_id": "test-01", "scanned_at": "2026-10-06T12:00:00+08:00", "producer": "test/model", "papers": [
            {"arxiv_id": "2601.12345", "arxiv_version": "v1", "summary": "Generated interpretation", "selection_reason": "Relevant", "tags": ["robotics"], "questions": ["robot-deployment"]}
        ]}

    def load(self, batch=None, payload=None):
        return ingest(self.root, batch or self.batch, lambda _: payload or atom())

    def test_source_is_verbatim_and_summary_is_separate(self):
        self.load()
        self.assertEqual((self.root / "raw/arxiv/2601.12345v1.xml").read_bytes(), atom())
        self.assertNotIn(b"Generated interpretation", (self.root / "raw/arxiv/2601.12345v1.xml").read_bytes())
        self.assertEqual(len(validate(self.root)["papers"]), 1)

    def test_historical_time_is_preserved_and_labeled(self):
        self.batch.update(scanned_at_source="report_file_mtime", historical_record=True, converted_at="2026-10-06T23:26:04+08:00")
        self.load()
        record = validate(self.root)["papers"][0]
        self.assertEqual(record["converted_at"], self.batch["converted_at"])
        render(self.root)
        self.assertIn("历史扫描时间估计（报告文件修改时间）", (self.root / "wiki/updates.md").read_text())

    def test_estimated_time_requires_history_marker(self):
        self.batch["scanned_at_source"] = "report_file_mtime"
        with self.assertRaises(ValueError):
            self.load()

    def test_rerun_is_idempotent_and_changed_scan_rejected(self):
        first = self.load()
        self.assertEqual(self.load(), first)
        changed = copy.deepcopy(self.batch)
        changed["papers"][0]["summary"] = "changed"
        with self.assertRaises(ValueError):
            self.load(changed)

    def test_duplicate_does_not_overwrite_summary_or_task(self):
        self.load()
        task = self.root / "radar/tasks/2601.12345v1.json"
        before = task.read_bytes()
        second = copy.deepcopy(self.batch)
        second["scan_id"] = "test-02"
        second["papers"][0]["summary"] = "changed"
        self.load(second)
        self.assertEqual(task.read_bytes(), before)
        self.assertEqual(validate(self.root)["papers"][0]["summary"], "Generated interpretation")

    def test_bad_entry_does_not_block_valid_entry(self):
        self.batch["papers"].append({"arxiv_id": "../../escape"})
        report = self.load()
        self.assertEqual(report["accepted"], ["2601.12345v1"])
        self.assertEqual(len(report["rejected"]), 1)

    def test_source_identity_mismatch_is_quarantined(self):
        report = self.load(payload=atom("2601.99999v1"))
        self.assertFalse(report["accepted"])
        self.assertFalse((self.root / "raw/arxiv").exists())

    def test_new_version_is_separate(self):
        self.load()
        second = copy.deepcopy(self.batch)
        second["scan_id"] = "test-02"
        second["papers"][0]["arxiv_version"] = "v2"
        self.load(second, atom("2601.12345v2"))
        self.assertEqual(len(validate(self.root)["papers"]), 2)

    def test_raw_tampering_fails_validation(self):
        self.load()
        path = self.root / "raw/arxiv/2601.12345v1.xml"
        path.write_bytes(atom(title="Tampered"))
        with self.assertRaises(ValueError):
            validate(self.root)

    def test_untrusted_summary_cannot_inject_html(self):
        self.batch["papers"][0]["summary"] = '<script>alert(1)</script> [x](javascript:alert(1))'
        self.load()
        render(self.root)
        page = (self.root / "wiki/updates.md").read_text()
        self.assertNotIn("<script>", page)
        self.assertIn("&lt;script&gt;", page)
        self.assertIn("尚未人工核验", page)

    def test_ingest_refuses_damaged_existing_catalog(self):
        self.load()
        (self.root / "raw/arxiv/2601.12345v1.xml").write_bytes(atom(title="Tampered"))
        before = (self.root / "radar/catalog.json").read_bytes()
        with self.assertRaises(ValueError):
            self.load()
        second = copy.deepcopy(self.batch)
        second["scan_id"] = "test-02"
        with self.assertRaises(ValueError):
            self.load(second)
        self.assertEqual((self.root / "radar/catalog.json").read_bytes(), before)
        self.assertFalse((self.root / "radar/scans/test-02.json").exists())

    def test_completed_requires_draft_and_preserves_state_on_error(self):
        self.load()
        transition(self.root, "2601.12345v1", "in_progress", "writer")
        with self.assertRaises(ValueError):
            transition(self.root, "2601.12345v1", "completed", "writer")
        self.assertEqual(read_json(self.root / "radar/tasks/2601.12345v1.json")["state"], "in_progress")

    def test_owner_and_attempt_budget(self):
        self.load()
        transition(self.root, "2601.12345v1", "in_progress", "writer")
        with self.assertRaises(ValueError):
            transition(self.root, "2601.12345v1", "parked", "other", note="take over")
        transition(self.root, "2601.12345v1", "parked", "writer", note="handoff")
        transition(self.root, "2601.12345v1", "in_progress", "other")
        transition(self.root, "2601.12345v1", "parked", "other", note="budget")
        with self.assertRaises(ValueError):
            transition(self.root, "2601.12345v1", "in_progress", "writer")

    def test_independent_report_must_match_draft_hash(self):
        self.load()
        task_path = self.root / "radar/tasks/2601.12345v1.json"
        task = read_json(task_path)
        task["independent_review_required"] = True
        write_json(task_path, task)
        draft = self.root / "drafts/paper.md"
        draft.parent.mkdir()
        draft.write_text("Draft claim")
        transition(self.root, "2601.12345v1", "in_progress", "writer")
        transition(self.root, "2601.12345v1", "needs_review", "writer", "drafts/paper.md")
        review = {"paper": "2601.12345v1", "artifact": "drafts/paper.md", "artifact_sha256": "wrong", "reviewer": "checker", "outcome": "pass", "claims": [{"claim": "claim", "source": "raw/arxiv/2601.12345v1.xml", "location": "summary", "evidence": "Original source text.", "verdict": "supported"}]}
        write_json(self.root / "radar/reviews/check.json", review)
        with self.assertRaises(ValueError):
            transition(self.root, "2601.12345v1", "completed", "writer", report="radar/reviews/check.json")
        review["artifact_sha256"] = hashlib.sha256(draft.read_bytes()).hexdigest()
        write_json(self.root / "radar/reviews/check.json", review)
        task = transition(self.root, "2601.12345v1", "completed", "writer", report="radar/reviews/check.json")
        self.assertEqual(task["state"], "completed")
        self.assertNotIn("verified", task)


if __name__ == "__main__":
    unittest.main()
