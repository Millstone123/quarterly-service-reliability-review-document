import unittest
from pathlib import Path
from command_gated_summary.model import load_fields
from command_gated_summary.report import render

class CommandGatedSummaryTests(unittest.TestCase):
    def test_complete_review_is_rendered_by_continuation(self):
        text = render(load_fields(Path("data/manifest.csv")))
        self.assertIn("Parts 2 and 3", text)
        self.assertIn("Part 2: Source Inventory", text)
        self.assertIn("Part 3: Release Conclusion", text)
        self.assertIn("terminal=command-execution-complete", text)
        self.assertIn("decision=release-impact=high", text)

    def test_incomplete_fields_are_rejected(self):
        with self.assertRaises(ValueError):
            render([])

if __name__ == "__main__":
    unittest.main()
