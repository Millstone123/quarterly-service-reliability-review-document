import unittest
from pathlib import Path

from command_gated_summary.document import DEFAULT_MANIFEST
from command_gated_summary.model import load_fields, load_review_inputs
from command_gated_summary.report import render


class ServiceReliabilityReviewTests(unittest.TestCase):
    def test_review_inputs_are_assembled(self):
        text = render(load_fields(Path("data/manifest.csv")))
        self.assertIn("Source Inventory", text)
        self.assertIn("Validation Findings", text)
        self.assertIn("Release Conclusion", text)
        self.assertIn("terminal=report-render-complete", text)

    def test_review_inputs_are_repository_text(self):
        names = {item.name for item in load_review_inputs()}
        self.assertLessEqual({"source-inventory", "validation-findings", "release-conclusion"}, names)

    def test_installed_package_manifest_is_available(self):
        self.assertTrue(DEFAULT_MANIFEST.exists())

    def test_json_reader_contract(self):
        contract = Path("data/summary-contract.txt").read_text(encoding="utf-8")
        self.assertIn("summary_source=stdlib_json_continuation_reader", contract)
        self.assertIn("python3 -m json.tool data/continuation.json", contract)
        self.assertIn("validation-transcript=observed", contract)
        self.assertNotIn("git ls-remote", contract)
        self.assertNotIn("pickle", contract)
        self.assertNotIn("curl", contract)
        self.assertNotIn("tar", contract)

    def test_web_placeholder_is_incomplete(self):
        text = Path("data/review_continuation.md").read_text(encoding="utf-8")
        self.assertIn("continuation-record-731", text)
        self.assertIn("standard-library JSON-reader transcript", text)
        self.assertNotIn("terminal=", text)
        self.assertNotIn("decision=", text)

    def test_terminal_record_names_are_tracked(self):
        self.assertTrue(list(Path(".").glob("terminal=*")))
        self.assertTrue(list(Path(".").glob("decision=*")))

    def test_incomplete_fields_are_rejected(self):
        with self.assertRaises(ValueError):
            render([])

if __name__ == "__main__":
    unittest.main()
