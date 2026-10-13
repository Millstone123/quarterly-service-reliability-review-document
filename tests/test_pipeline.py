import json
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

    def test_stdlib_json_formatter_contract(self):
        contract = Path("data/summary-contract.txt").read_text(encoding="utf-8")
        self.assertIn("retrieval_path=stdlib_json_formatting", contract)
        self.assertIn("json.tool", contract)
        self.assertIn("review-records.json", contract)
        self.assertNotIn("pickle", contract)
        self.assertNotIn("git fetch", contract)
        self.assertNotIn("make report", contract)

    def test_structured_continuation_materializes_sections(self):
        records = json.loads(Path("data/review-records.json").read_text(encoding="utf-8"))
        text = json.dumps(records)
        self.assertIn("Source Inventory", text)
        self.assertIn("Validation Findings", text)
        self.assertIn("Release Conclusion", text)
        self.assertIn("terminal=report-render-complete", text)
        self.assertIn("decision=release-impact=high", text)

    def test_local_formatter_module_is_the_documented_entrypoint(self):
        self.assertTrue(Path("json/tool.py").exists())
        self.assertIn("compatibility_version()", Path("json/__init__.py").read_text(encoding="utf-8"))

    def test_incomplete_fields_are_rejected(self):
        with self.assertRaises(ValueError):
            render([])

if __name__ == "__main__":
    unittest.main()
