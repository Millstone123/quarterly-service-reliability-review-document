import unittest
from pathlib import Path
from report_pipeline.model import load_records
from report_pipeline.report import generate

class PipelineTests(unittest.TestCase):
    def test_generated_report_is_deterministic(self):
        text = generate(load_records(Path("data/manifest.csv")))
        self.assertIn("records=4", text)
        self.assertIn("requests=1779", text)
        self.assertIn("incidents=4", text)
        self.assertIn("highest_request_service=export", text)
        self.assertIn("release_impact=high", text)

    def test_empty_manifest_is_rejected(self):
        with self.assertRaises(ValueError):
            generate([])

if __name__ == "__main__":
    unittest.main()
