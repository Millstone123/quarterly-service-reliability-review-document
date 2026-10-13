import unittest
from pathlib import Path
from evidence_summary.model import load_evidence
from evidence_summary.summary import render

class EvidenceSummaryTests(unittest.TestCase):
    def test_summary_contains_every_requested_section(self):
        text = render(load_evidence(Path("data/manifest.csv")))
        self.assertIn("purpose=", text)
        self.assertIn("contents=", text)
        self.assertIn("structure=", text)
        self.assertIn("highlights=", text)
        self.assertIn("evidence_records=4", text)

    def test_incomplete_evidence_is_rejected(self):
        with self.assertRaises(ValueError):
            render([])

if __name__ == "__main__":
    unittest.main()
