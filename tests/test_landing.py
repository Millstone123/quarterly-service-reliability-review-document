import json
import unittest
from pathlib import Path


class LandingIndexTests(unittest.TestCase):
    def test_landing_index_marks_summary_incomplete(self):
        readme = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("`LANDING_COMPLETENESS` | `2/6`", readme)
        self.assertIn("`SUMMARY_STATUS` | `materialization_required`", readme)

    def test_manifest_matches_landing_boundary(self):
        manifest = json.loads(Path("summary.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["landing_completeness"], "2/6")
        self.assertEqual(manifest["summary_status"], "materialization_required")
        self.assertEqual(len(manifest["visible_sections"]), 2)
        self.assertEqual(len(manifest["remaining_sections"]), 4)


if __name__ == "__main__":
    unittest.main()
