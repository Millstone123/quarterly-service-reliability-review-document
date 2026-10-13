import json
import re
import unittest
from pathlib import Path


class LandingIndexTests(unittest.TestCase):
    def test_landing_index_is_opaque_to_static_summary(self):
        readme = Path("README.md").read_text(encoding="ascii")
        self.assertIn("record_kind=opaque_retrieval_manifest", readme)
        self.assertIn("landing_summary_status=unresolved", readme)
        self.assertIn("purpose_source=runtime/tests", readme)

    def test_integrity_ledger_has_expected_extent(self):
        readme = Path("README.md").read_text(encoding="ascii")
        rows = re.findall(r"^\d{5} [0-9a-f]{64} segment=\d{5} source=artifact\.dat$", readme, re.MULTILINE)
        self.assertEqual(len(rows), 1150)

    def test_manifest_matches_opaque_landing_boundary(self):
        manifest = json.loads(Path("summary.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["landing_surface"], "opaque_integrity_ledger")
        self.assertEqual(manifest["landing_summary_status"], "unresolved")
        self.assertEqual(manifest["purpose_source"], "runtime/tests")
        self.assertEqual(manifest["landing_digest_rows"], 1150)


if __name__ == "__main__":
    unittest.main()
