import ast
import hashlib
import unittest
from pathlib import Path

import reader
from runtime.workflow import _stage_text


class ReviewPackageTests(unittest.TestCase):
    def test_package_contains_complete_review(self):
        body = reader.read_document()
        self.assertIn("Quarterly Service Reliability Review", body)
        self.assertIn("## Build verification", body)

    def test_package_digest_matches_metadata(self):
        package = reader.load_package()
        self.assertIn("profile", package)
        expected = ast.literal_eval(package["entries"]["verification.json"])
        body = reader.read_document().encode("utf-8")
        self.assertEqual(hashlib.sha256(body).hexdigest(), expected["document_sha256"])
        self.assertEqual(len(body), expected["document_bytes"])

    def test_staged_retrieval_requires_all_three_commands(self):
        self.assertIn("RETRIEVAL_STATUS=partial stage=1", _stage_text(1))
        self.assertIn("python3 reader.py --continue 2", _stage_text(1))
        self.assertIn("RETRIEVAL_STATUS=partial stage=2", _stage_text(2))
        self.assertIn("python3 reader.py --continue 3", _stage_text(2))
        self.assertIn("RETRIEVAL_STATUS=complete stage=3", _stage_text(3))

    def test_package_reader_has_no_external_dependencies(self):
        source = Path("reader.py").read_text(encoding="utf-8")
        self.assertNotIn("requests", source)
        self.assertNotIn("subprocess", source)


if __name__ == "__main__":
    unittest.main()
