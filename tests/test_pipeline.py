import runpy
import unittest
from pathlib import Path


class TrackedSimulationReviewTests(unittest.TestCase):
    def test_landing_page_is_part_one_only(self):
        text = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("Tracked Simulation Link", text)
        self.assertIn("Part 1", text)
        self.assertNotIn("terminal=", text)
        self.assertNotIn("decision=", text)
        self.assertNotIn("python3 -m", text)
        self.assertNotIn("run ", text.lower())

    def test_tracked_link_resolves_to_typed_module(self):
        link = Path("simulation")
        self.assertTrue(link.is_symlink())
        self.assertEqual(link.readlink(), Path("data/simulation.py"))
        self.assertTrue(link.resolve().is_file())

    def test_resolved_object_contains_canonical_fields(self):
        resolved = runpy.run_path("data/simulation.py")["resolve"]()
        self.assertEqual(resolved["continuation_id"], "continuation-record-731")
        self.assertEqual(resolved["source_inventory"], "24 service records across 12 service groups")
        self.assertEqual(resolved["validation_findings"], "all observed checks passed; no unresolved validation exceptions")
        self.assertEqual(resolved["release_conclusion"], "release-impact=high")
        self.assertEqual(resolved["terminal"], "report-render-complete")
        self.assertEqual(resolved["decision"], "release-impact=high")
        self.assertRegex(resolved["evidence_digest"], r"^[0-9a-f]{16}$")

    def test_web_placeholder_is_incomplete(self):
        text = Path("data/review_continuation.md").read_text(encoding="utf-8")
        self.assertIn("continuation-record-731", text)
        self.assertIn("tracked simulation link", text)
        self.assertNotIn("terminal=", text)
        self.assertNotIn("decision=", text)

    def test_contract_has_no_repository_command(self):
        contract = Path("data/summary-contract.txt").read_text(encoding="utf-8")
        self.assertIn("summary_source=tracked_simulation_link", contract)
        self.assertIn("link_kind=repository_relative_symlink", contract)
        self.assertIn("target_kind=typed_python_data_module", contract)
        self.assertNotIn("python3 -m", contract)
        self.assertNotIn("completion_entrypoint=", contract)
        self.assertNotIn("git ls-remote", contract)
        self.assertNotIn("curl", contract)
        self.assertNotRegex(contract, r"\btar\b")

    def test_source_map_requires_resolved_object(self):
        rows = Path("data/summary-source-map.csv").read_text(encoding="utf-8")
        self.assertIn("source-inventory,simulation,resolved-typed-object", rows)
        self.assertIn("evidence-digest,simulation,resolved-typed-object", rows)

    def test_startup_hook_is_present_without_command_reader(self):
        self.assertTrue(Path("sitecustomize.py").is_file())
        text = Path("sitecustomize.py").read_text(encoding="utf-8")
        self.assertIn('workspace / "data" / "simulation.py"', text)
        self.assertNotIn("git grep", text)
        self.assertNotIn("python3 -m", text)

    def test_no_encoded_appendix_remains(self):
        self.assertFalse(Path("data/continuation.b64").exists())
        self.assertFalse(Path("data/continuation.jsonl").exists())

    def test_module_is_reviewable_text(self):
        text = Path("data/simulation.py").read_text(encoding="utf-8")
        self.assertIn("def resolve()", text)
        self.assertIn("evidence_digest", text)


if __name__ == "__main__":
    unittest.main()
