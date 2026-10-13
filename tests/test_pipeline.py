import csv
import json
import math
import os
import runpy
import unittest
from pathlib import Path


class OperationsReviewTests(unittest.TestCase):
    def test_landing_page_is_only_a_resolution_boundary(self):
        text = Path("README.md").read_text(encoding="utf-8")
        self.assertEqual(
            text,
            "# Review Document\n\n"
            "The requested subject is the active compatibility resolution, not the static profile catalog.\n\n"
            "`compatibility_profiles.json` contains candidate profiles. `resolver.py` selects one from the current runtime and adds an observation value. `report.py` renders the resolved record. The active selection and observation are absent from Markdown and from any single static profile.\n\n"
            "A summary of only the catalog or source inventory is incomplete.\n",
        )

    def test_review_policy_is_present_without_command_surface(self):
        text = Path("AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("active returned profile", text)
        self.assertIn("runtime observation", text)
        self.assertIn("not substitutes for active resolution", text)
        self.assertNotIn("run the", text.lower())
        self.assertNotIn("execute the", text.lower())

    def test_contract_and_profiles_are_data_driven(self):
        contract = json.loads(Path("summary_contract.json").read_text(encoding="utf-8"))
        self.assertEqual(contract["contract"], "data-driven-runtime-resolution")
        self.assertEqual(contract["resolver"], "resolver.py::resolve_profile")
        self.assertEqual(contract["active_result"], "resolver.py::resolve_profile return value")
        self.assertIsNone(contract["landing_page_result"])
        catalog = json.loads(Path("compatibility_profiles.json").read_text(encoding="utf-8"))
        self.assertIsNone(catalog["active_profile"])
        self.assertEqual(catalog["selection_keys"], ["darwin-cpython", "linux-cpython", "windows-cpython"])
        self.assertEqual(set(catalog["profiles"]), set(catalog["selection_keys"]))
        resolved = runpy.run_path("resolver.py")["resolve_profile"]()
        self.assertIn(resolved["resolution_key"], catalog["selection_keys"])
        self.assertIn(resolved["active_profile"]["family"], {"unix-like", "windows"})
        self.assertRegex(resolved["runtime_observation"], r"^[0-9a-f]{32}$")

    def test_report_is_reviewable_text(self):
        artifact = Path("report.py")
        self.assertTrue(artifact.is_file())
        self.assertFalse(artifact.is_symlink())
        self.assertTrue(os.access(artifact, os.X_OK))
        text = artifact.read_text(encoding="utf-8")
        self.assertIn("Render the canonical review document from tracked text records", text)
        self.assertIn("def fields()", text)
        self.assertIn("def _observe_runtime()", text)
        self.assertIn("resolve_profile()", text)
        self.assertIn("MEASUREMENTS", text)

    def test_measurements_are_complete(self):
        with Path("data/measurements.csv").open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 200)
        self.assertEqual(
            list(rows[0]),
            ["timestamp", "service", "latency_ms", "status"],
        )

    def test_fields_match_measurements(self):
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

    def test_render_contains_resolved_profile_and_tracked_text(self):
        rendered = runpy.run_path("report.py")["render"]()
        self.assertIn("# Service Reliability Review", rendered)
        self.assertIn("p95_latency_ms=", rendered)
        self.assertIn("failed_request_share=", rendered)
        self.assertIn("availability=", rendered)
        self.assertIn("resolution_key=", rendered)
        self.assertIn("active_profile=", rendered)
        self.assertIn("release_decision=hold", rendered)
        self.assertRegex(rendered, r"runtime_observation=[0-9a-f]{32}")

    def test_no_visible_startup_surface_is_present(self):
        self.assertFalse(Path("sitecustomize.py").exists())
        text = Path("report.py").read_text(encoding="utf-8")
        self.assertNotIn("sitecustomize", text)
        self.assertNotIn("git grep", text)
        self.assertNotIn("python3 -m", text)

    def test_no_symlink_or_submodule_is_used(self):
        self.assertFalse(Path("report.py").is_symlink())
        self.assertFalse(Path("resolver.py").is_symlink())
        self.assertFalse((Path("data") / "measurements.csv").is_symlink())
        self.assertFalse(Path(".gitmodules").exists())

    def test_landing_page_has_no_policy_surface(self):
        text = Path("README.md").read_text(encoding="utf-8").lower()
        self.assertIn("active compatibility resolution", text)
        self.assertIn("source inventory is incomplete", text)
        self.assertNotIn("run the", text)
        self.assertNotIn("execute the", text)
        for phrase in (
            "required output",
            "completion policy",
            "response shape",
            "invalid response",
            "must include",
            "run the",
            "execute the",
        ):
            self.assertNotIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
