import unittest
from pathlib import Path
from command_gated_summary.model import load_fields, load_review_inputs
from command_gated_summary.report import render

class CommandGatedSummaryTests(unittest.TestCase):
    def test_distributed_inputs_are_assembled(self):
        text = render(load_fields(Path("data/manifest.csv")))
        self.assertIn("Part 2: Source Inventory", text)
        self.assertIn("Part 3: Release Conclusion", text)
        self.assertIn("source inventory records", text)
        self.assertIn("terminal=command-execution-complete", text)

    def test_review_inputs_are_repository_text(self):
        names = {item.name for item in load_review_inputs()}
        self.assertLessEqual({"source-inventory", "validation-findings", "release-conclusion"}, names)

    def test_incomplete_fields_are_rejected(self):
        with self.assertRaises(ValueError):
            render([])

if __name__ == "__main__":
    unittest.main()
