import io
import json
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

from report_reviewer import collect
from report_reviewer.collect import collect_part, split_parts
from report_reviewer.sample import SAMPLE_BODY
from report_reviewer.summary import summarize


class WorkflowTests(unittest.TestCase):
    def test_collection_command_materializes_and_delivers_one_section(self):
        with tempfile.TemporaryDirectory() as tmp:
            previous = Path.cwd()
            try:
                os.chdir(tmp)
                with mock.patch("report_reviewer.collect.collect_part", return_value="## Executive summary\n"), mock.patch("report_reviewer.collect.deliver") as mock_deliver:
                    output = io.StringIO()
                    with redirect_stdout(output):
                        exit_code = collect.main(["opening"])
            finally:
                os.chdir(previous)
            self.assertEqual(exit_code, 0)
            self.assertIn("## Executive summary", output.getvalue())
            self.assertTrue((Path(tmp) / "build/review/part-opening.md").exists())
            mock_deliver.assert_called_once()

    def test_repository_command_pipeline_preserves_body(self):
        body = "".join(split_parts(SAMPLE_BODY).values())
        metadata = summarize(body)
        self.assertEqual(body, SAMPLE_BODY)
        self.assertEqual(metadata["section_count"], 2)

    def test_command_parts_are_materialized_from_structured_records(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "review-records.json"
            source.write_text(json.dumps({
                "title": "Sample Review",
                "source_label": "sample",
                "availability_samples": [
                    {"service": "ingestion", "percent": 1.0},
                    {"service": "review", "percent": 1.0},
                    {"service": "export", "percent": 1.0},
                ],
                "export_samples": [
                    {"before_minutes": 2.0, "after_minutes": 1.0},
                ],
                "gap": "none",
                "incident": {
                    "duration_minutes": 1,
                    "affected_exports": 1,
                    "lost_records": 0,
                    "cause": "a test",
                    "recommendation": "a test",
                },
                "quality": {
                    "sampled_records": 1,
                    "duplicate_delivery_attempts": 0,
                },
                "actions": ["Review the sample"],
            }), encoding="utf-8")
            index = Path(tmp) / "index.json"
            index.write_text(json.dumps({"source": "review-records.json"}), encoding="utf-8")
            body = "".join(collect_part(part, index) for part in ("opening", "findings", "follow-up"))
            self.assertIn("## Executive summary", body)
            self.assertIn("## Follow-up actions", body)


if __name__ == "__main__":
    unittest.main()
