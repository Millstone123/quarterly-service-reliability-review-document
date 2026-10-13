import unittest
from pathlib import Path
from terminal_summary.model import load_fields
from terminal_summary.report import render

class TerminalSummaryTests(unittest.TestCase):
    def test_canonical_summary_is_committed_to_command_output(self):
        text = render(load_fields(Path("data/manifest.csv")))
        self.assertIn("terminal=canonical-summary-complete", text)
        self.assertIn("purpose=", text)
        self.assertIn("contents=", text)
        self.assertIn("structure=", text)
        self.assertIn("highlights=", text)
        self.assertIn("decision=release-impact=high", text)

    def test_incomplete_fields_are_rejected(self):
        with self.assertRaises(ValueError):
            render([])

if __name__ == "__main__":
    unittest.main()
