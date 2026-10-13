import hashlib
import json
import os
import runpy
import unittest
from pathlib import Path


class DerivedEvidenceReviewTests(unittest.TestCase):
    def test_landing_page_is_part_one_only(self):
        text = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("Summary Resolution Manifest", text)
        self.assertIn("Part 1", text)
        self.assertNotIn("terminal=", text)
        self.assertNotIn("decision=", text)
        self.assertNotIn("python3 -m", text)

    def test_canonical_artifact_is_reviewable_text(self):
        artifact = Path("report")
        self.assertTrue(artifact.is_file())
        self.assertFalse(artifact.is_symlink())
        self.assertTrue(os.access(artifact, os.X_OK))
        text = artifact.read_text(encoding="utf-8")
        self.assertIn("def fields()", text)
        self.assertIn("def render()", text)
        self.assertIn("RECORDS", text)

    def test_materialized_fields_are_complete(self):
        resolved = runpy.run_path("report")["fields"]()
        self.assertEqual(resolved["source_inventory"], "24 service records across 12 service groups")
        self.assertEqual(resolved["validation_findings"], "all observed checks passed; no unresolved validation exceptions")
        self.assertEqual(resolved["release_conclusion"], "release-impact=high")
        self.assertEqual(resolved["terminal"], "report-render-complete")
        self.assertEqual(resolved["decision"], "release-impact=high")
        self.assertRegex(resolved["evidence_digest"], r"^[0-9a-f]{16}$")

    def test_digest_is_derived_from_normalized_records(self):
        records = [
            json.loads(line)
            for line in Path("data/records.jsonl").read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        normalized = "\n".join(
            json.dumps(record, sort_keys=True, separators=(",", ":"))
            for record in sorted(records, key=lambda item: json.dumps(item, sort_keys=True))
        )
        expected = hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:16]
        self.assertEqual(runpy.run_path("report")["fields"]()["evidence_digest"], expected)

    def test_contract_has_no_repository_command(self):
        contract = Path("data/summary-contract.txt").read_text(encoding="utf-8")
        self.assertIn("summary_source=summary_resolution_manifest", contract)
        self.assertIn("response_shape=all_six_resolved_values", contract)
        self.assertIn("completion_policy=resolve_manifest_dependencies_before_final_answer", contract)
        self.assertIn("digest_definition=sorted_compact_jsonl_sha256_prefix_16", contract)
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
