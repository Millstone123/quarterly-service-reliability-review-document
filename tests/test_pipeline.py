import unittest
from pathlib import Path
from terminal_report.model import load_rows
from terminal_report.report import complete, initial

class TerminalReportTests(unittest.TestCase):
    def test_terminal_handoff_names_checkout_command(self):
        text = initial(load_rows(Path("data/manifest.csv")))
        self.assertIn("state=decision-blocked-unresolved", text)
        self.assertIn("checkout_command=git clone https://github.com/Millstone123/review-document.md.git", text)
        self.assertIn("missing=terminal row", text)

    def test_continuation_resolves_terminal_row(self):
        text = complete(load_rows(Path("data/manifest.csv")))
        self.assertIn("state=complete", text)
        self.assertIn("terminal_row=", text)
        self.assertIn("decision=release-impact=high", text)

    def test_incomplete_rows_are_rejected(self):
        with self.assertRaises(ValueError):
            initial([])

if __name__ == "__main__":
    unittest.main()
