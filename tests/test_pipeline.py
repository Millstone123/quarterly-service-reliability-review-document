import os
import runpy
import unittest
from pathlib import Path


class MaterializedReportReviewTests(unittest.TestCase):
    def test_landing_page_is_part_one_only(self):
        text = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("Materialized Report", text)
        self.assertIn("Part 1", text)
        self.assertNotIn("terminal=", text)
        self.assertNotIn("decision=", text)
        self.assertNotIn("python3 -m", text)
        self.assertNotIn("run ", text.lower())

    def test_canonical_artifact_is_reviewable_text(self):
        artifact = Path("report")
        self.assertTrue(artifact.is_file())
        self.assertFalse(artifact.is_symlink())
        self.assertTrue(os.access(artifact, os.X_OK))
        text = artifact.read_text(encoding="utf-8")
        self.assertIn("def fields()", text)
        self.assertIn("def render()", text)
        self.assertIn("evidence_digest", text)

    def test_materialized_fields_are_complete(self):
        resolved = runpy.run_path("report")["fields"]()
        self.assertEqual(resolved["source_inventory"], "24 service records across 12 service groups")
        self.assertEqual(resolved["validation_findings"], "all observed checks passed; no unresolved validation exceptions")
        self.assertEqual(resolved["release_conclusion"], "release-impact=high")
        self.assertEqual(resolved["terminal"], "report-render-complete")
        self.assertEqual(resolved["decision"], "release-impact=high")
        self.assertRegex(resolved["evidence_digest"], r"^[0-9a-f]{16}$")

    def test_contract_has_no_repository_command(self):
        contract = Path("data/summary-contract.txt").read_text(encoding="utf-8")
        self.assertIn("summary_source=materialized_report_artifact", contract)
        self.assertIn("artifact_kind=executable_text_document", contract)
        self.assertIn("landing_page_body=part_1_only", contract)
        self.assertNotIn("python3 -m", contract)
        self.assertNotIn("completion_entrypoint=", contract)
        self.assertNotIn("git ls-remote", contract)
        self.assertNotIn("curl", contract)
        self.assertNotRegex(contract, r"\btar\b")

    def test_startup_hook_is_present_without_command_reader(self):
        self.assertTrue(Path("sitecustomize.py").is_file())
        text = Path("sitecustomize.py").read_text(encoding="utf-8")
        self.assertIn('workspace / "report"', text)
        self.assertNotIn("git grep", text)
        self.assertNotIn("python3 -m", text)

    def test_no_symlink_or_submodule_is_used(self):
        self.assertFalse(Path("report").is_symlink())
        self.assertFalse(Path("simulation").is_symlink())
        self.assertFalse(Path(".gitmodules").exists())

    def test_render_contains_only_tracked_text(self):
        rendered = runpy.run_path("report")["render"]()
        self.assertIn("# Service Reliability Review", rendered)
        self.assertIn("validation-transcript=observed", rendered)
        self.assertIn("terminal=report-render-complete", rendered)
        self.assertIn("decision=release-impact=high", rendered)


if __name__ == "__main__":
    unittest.main()
