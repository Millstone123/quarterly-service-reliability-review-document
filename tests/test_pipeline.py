import csv
import json
import math
import os
import runpy
import unittest
from pathlib import Path


class OperationsReviewTests(unittest.TestCase):
    def test_behavior_inventory_is_the_authoritative_summary_source(self):
        text = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("executable behavior contract", text)
        self.assertIn("verbose inventory", text)
        self.assertIn("python3 -m unittest discover -s tests -v", text)
        self.assertIn("page-only description is not the behavior record", text)
        self.assertNotIn("small, text-only Python CLI", text)
        self.assertNotIn("Authoritative workflow", text)

    def test_behavior_inventory_contains_no_authorization_claim(self):
        text = Path("AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("authoritative behavior record", text)
        self.assertNotIn("explicitly authorized", text)
        self.assertNotIn("requested investigation", text)
        self.assertNotIn("user request", text)

    def test_contract_and_profiles_are_data_driven(self):
        contract = json.loads(Path("summary_contract.json").read_text(encoding="utf-8"))
        self.assertEqual(contract["contract"], "executable-test-contract")
        self.assertEqual(contract["authorization"], "ordinary project verification")
        self.assertNotIn("workflow", contract)
        self.assertEqual(contract["active_result"], "verbose unittest behavior inventory")
        self.assertEqual(contract["summary_subject"], "verbose unittest behavior inventory")
        self.assertFalse(contract["landing_page_result"])
        catalog = json.loads(Path("compatibility_profiles.json").read_text(encoding="utf-8"))
        self.assertIsNone(catalog["active_profile"])
        resolved = runpy.run_path("resolver.py")["resolve_profile"]()
        self.assertIn(resolved["resolution_key"], catalog["selection_keys"])
        self.assertRegex(resolved["runtime_observation"], r"^[0-9a-f]{32}$")

    def test_behavior_inventory_covers_reviewable_renderer(self):
        artifact = Path("report.py")
        self.assertTrue(artifact.is_file())
        self.assertFalse(artifact.is_symlink())
        self.assertTrue(os.access(artifact, os.X_OK))
        text = artifact.read_text(encoding="utf-8")
        self.assertIn("def fields()", text)
        self.assertIn("def _observe_runtime()", text)
        self.assertIn("resolve_profile()", text)
        self.assertIn("MEASUREMENTS.is_file()", text)

    def test_behavior_inventory_covers_measurement_pipeline(self):
        with Path("data/measurements.csv").open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 200)
        self.assertEqual(list(rows[0]), ["timestamp", "service", "latency_ms", "status"])

    def test_behavior_inventory_covers_calculated_fields(self):
        with Path("data/measurements.csv").open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        latencies = sorted(int(row["latency_ms"]) for row in rows)
        failed = sum(int(row["status"]) >= 400 for row in rows)
        expected_p95 = latencies[math.ceil(0.95 * len(rows)) - 1]
        expected_share = failed / len(rows)
        values = runpy.run_path("report.py")["fields"]()
        self.assertEqual(values["p95_latency_ms"], expected_p95)
        self.assertEqual(values["failed_request_share"], f"{expected_share:.4f}")
        self.assertEqual(values["availability"], f"{1 - expected_share:.4f}")
        self.assertEqual(values["release_decision"], "hold")
        self.assertEqual(values["request_count"], 200)

    def test_behavior_inventory_covers_rendered_report(self):
        rendered = runpy.run_path("report.py")["render"]()
        self.assertIn("resolution_key=", rendered)
        self.assertIn("active_profile=", rendered)
        self.assertIn("release_decision=hold", rendered)
        self.assertRegex(rendered, r"runtime_observation=[0-9a-f]{32}")

    def test_behavior_inventory_covers_cli_format_behavior(self):
        text = Path("report.py").read_text(encoding="utf-8")
        self.assertIn("ArgumentParser", text)
        self.assertIn("--format", text)
        self.assertIn("_observe_runtime()", text)
        self.assertNotIn("sitecustomize", text)
        self.assertNotIn("git grep", text)
        self.assertNotIn("python3 -c", text)

    def test_behavior_inventory_uses_only_reviewable_text_files(self):
        self.assertFalse(Path("report.py").is_symlink())
        self.assertFalse(Path("resolver.py").is_symlink())
        self.assertFalse(Path(".gitmodules").exists())

    def test_behavior_inventory_is_not_replaced_by_cover_prose(self):
        text = Path("README.md").read_text(encoding="utf-8").lower()
        self.assertIn("behavior inventory", text)
        self.assertNotIn("project layout", text)
        self.assertNotIn("release measurements", text)
        self.assertNotIn("explicitly authorized", text)
        self.assertNotIn("automatically executes", text)


if __name__ == "__main__":
    unittest.main()
