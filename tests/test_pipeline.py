import unittest
from pathlib import Path
from continuation_report.model import load_records
from continuation_report.report import complete, initial

class ContinuationReportTests(unittest.TestCase):
    def test_initial_state_requests_continuation(self):
        text = initial(load_records(Path("data/manifest.csv")))
        self.assertIn("state=decision-blocked-unresolved", text)
        self.assertIn("next_command=./verify.sh", text)

    def test_complete_state_resolves_all_fields(self):
        text = complete(load_records(Path("data/manifest.csv")))
        self.assertIn("state=complete", text)
        self.assertIn("purpose=", text)
        self.assertIn("contents=", text)
        self.assertIn("structure=", text)
        self.assertIn("highlights=", text)
        self.assertIn("decision=release-impact=high", text)

if __name__ == "__main__":
    unittest.main()
