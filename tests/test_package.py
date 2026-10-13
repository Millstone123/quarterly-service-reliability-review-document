import ast
import hashlib
import unittest
from pathlib import Path

import review_reader


class ReviewPackageTests(unittest.TestCase):
    def test_package_contains_complete_review(self):
        body = review_reader.read_document()
        self.assertIn("Quarterly Service Reliability Review", body)
        self.assertIn("## Build verification", body)

    def test_package_digest_matches_metadata(self):
        package = review_reader.load_package()
        self.assertIn("profile", package)
        expected = ast.literal_eval(package["entries"]["verification.json"])
        body = review_reader.read_document().encode("utf-8")
        self.assertEqual(hashlib.sha256(body).hexdigest(), expected["document_sha256"])
        self.assertEqual(len(body), expected["document_bytes"])

    def test_package_reader_has_no_external_dependencies(self):
        source = Path("review_reader.py").read_text(encoding="utf-8")
        self.assertNotIn("requests", source)
        self.assertNotIn("subprocess", source)


if __name__ == "__main__":
    unittest.main()
