import unittest
from pathlib import Path
from command_gated_summary.model import load_fields
from command_gated_summary.report import render

class CommandGatedSummaryTests(unittest.TestCase):
    def test_canonical_answer_is_rendered_after_command(self):
        text = render(load_fields(Path("data/manifest.csv")))
        self.assertIn("terminal=command-execution-complete", text)
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
