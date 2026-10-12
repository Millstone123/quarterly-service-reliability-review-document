import json
import tempfile
import unittest
from pathlib import Path

from report_reviewer.collect import load_source, split_parts
from report_reviewer.sample import SAMPLE_BODY
from report_reviewer.summary import summarize


class SummaryTests(unittest.TestCase):
    def test_load_source_resolves_repository_relative_index_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            repository = Path(tmp)
            data = repository / "data"
            data.mkdir()
            (data / "index.json").write_text(
                json.dumps({"source": "data/review-records.json"}),
                encoding="utf-8",
            )
            (data / "review-records.json").write_text('{"ok": true}', encoding="utf-8")
            previous = Path.cwd()
            try:
                import os
                os.chdir(repository)
                source = load_source(Path("data/index.json"))
            finally:
                os.chdir(previous)
            self.assertEqual(source, {"ok": True})

    def test_review_body_splits_into_command_parts(self):
        parts = split_parts(SAMPLE_BODY)
        self.assertEqual("".join(parts.values()), SAMPLE_BODY)
        self.assertTrue(parts["opening"].startswith("# Sample Review"))
        self.assertIn("## Follow-up actions", parts["follow-up"])

    def test_summary_reports_stable_structure(self):
        result = summarize(SAMPLE_BODY)
        self.assertTrue(result["body_sha256"])
        self.assertEqual(result["sections"], ["Executive summary", "Follow-up actions"])
        self.assertEqual(result["section_count"], 2)
        self.assertGreater(result["word_count"], 0)


if __name__ == "__main__":
    unittest.main()
