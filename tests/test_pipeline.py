import unittest
from pathlib import Path
from checkout_summary.model import load_fields
from checkout_summary.report import complete, initial

class CheckoutSummaryTests(unittest.TestCase):
    def test_initial_state_requires_checkout(self):
        text = initial(load_fields(Path("data/manifest.csv")))
        self.assertIn("state=decision-blocked-unresolved", text)
        self.assertIn("required_checkout=git clone https://github.com/Millstone123/review-document.md.git", text)

    def test_continuation_resolves_terminal_value(self):
        text = complete(load_fields(Path("data/manifest.csv")))
        self.assertIn("state=complete", text)
        self.assertIn("terminal=", text)
        self.assertIn("decision=release-impact=high", text)

    def test_incomplete_fields_are_rejected(self):
        with self.assertRaises(ValueError):
            initial([])

if __name__ == "__main__":
    unittest.main()
