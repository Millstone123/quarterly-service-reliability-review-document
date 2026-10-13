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

    def test_git_text_inventory_contract(self):
        contract = Path("data/summary-contract.txt").read_text(encoding="utf-8")
        self.assertIn("retrieval_path=git_read_only_file_search", contract)
        self.assertIn("git grep", contract)
        self.assertIn("data/review_continuation.md", contract)
        self.assertNotIn("pickle", contract)
        self.assertNotIn("curl", contract)
        self.assertNotIn("json.tool", contract)

    def test_continuation_materializes_sections(self):
        text = Path("data/review_continuation.md").read_text(encoding="utf-8")
        self.assertIn("continuation[-]record-731".replace("[-]", "-"), text)
        self.assertIn("Source Inventory", text)
        self.assertIn("Validation Findings", text)
        self.assertIn("Release Conclusion", text)
        self.assertIn("terminal=report-render-complete", text)
        self.assertIn("decision=release-impact=high", text)

    def test_incomplete_fields_are_rejected(self):
        with self.assertRaises(ValueError):
            render([])

if __name__ == "__main__":
    unittest.main()
