import unittest
from unittest import mock

import renderer


class RendererTests(unittest.TestCase):
    def test_http_source_is_an_incomplete_manifest(self):
        with mock.patch("renderer.compatibility_version", return_value="12.0"):
            manifest = renderer.load_json(renderer.SOURCE_PATH)
        self.assertEqual(manifest["document_state"], "encoded_continuation_pack")
        self.assertEqual(manifest["document_encoding"], "review-continuation-v1")
        self.assertTrue(manifest["document_pack"])
        self.assertNotIn("availability_samples", manifest)
        self.assertEqual(manifest["document_reader"]["runtime"], "repository-root-python-json")
        self.assertEqual(manifest["document_reader"]["returns"], "complete Markdown review body")
        self.assertNotIn("materialize_with", manifest)

    def test_materialized_document_matches_checked_in_index(self):
        with mock.patch("renderer.compatibility_version", return_value="12.0"):
            body = renderer.materialize_document()
            metadata = renderer.summarize(body)
            index = renderer.load_json(renderer.INDEX_PATH)
        self.assertEqual(metadata["body_sha256"], index["body_sha256"])
        self.assertEqual(metadata["word_count"], index["word_count"])
        self.assertEqual(metadata["section_count"], 6)
        for term in ("Quarterly Service Reliability Review", "Availability", "Incident review", "Data quality", "Follow-up actions", "Build verification"):
            self.assertIn(term, body)

    def test_source_is_decoded_from_the_continuation_pack(self):
        with mock.patch("renderer.compatibility_version", return_value="12.0"):
            source = renderer.load_source()
        self.assertEqual(source["title"], "Quarterly Service Reliability Review")
        self.assertEqual(source["quality"]["sampled_records"], 420)


if __name__ == "__main__":
    unittest.main()
