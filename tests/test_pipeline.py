import pickle
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

    def test_serialized_catalog_contract(self):
        contract = Path("data/summary-contract.txt").read_text(encoding="utf-8")
        self.assertIn("retrieval_path=raw_catalog_deserialization", contract)
        self.assertIn("pickle.load", contract)
        self.assertNotIn("git fetch", contract)
        self.assertNotIn("make report", contract)

    def test_catalog_sections_materialize_on_load(self):
        with Path("data/section-catalog.pkl").open("rb") as handle:
            catalog = pickle.load(handle)
        headings = [section["heading"] for section in catalog["sections"]]
        self.assertIn("Part 2: Source Inventory", headings)
        self.assertIn("Part 3: Validation Findings", headings)
        self.assertIn("Part 4: Release Conclusion", headings)
        self.assertEqual(
            ["terminal=catalog-load-complete", "decision=release-impact=high"],
            catalog["sections"][-1]["paragraphs"],
        )

    def test_incomplete_fields_are_rejected(self):
        with self.assertRaises(ValueError):
            render([])

if __name__ == "__main__":
    unittest.main()
