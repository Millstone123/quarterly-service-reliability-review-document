import unittest
from unittest import mock

import renderer


class RendererTests(unittest.TestCase):
    def test_http_source_is_an_incomplete_manifest(self):
        with mock.patch("renderer.compatibility_version", return_value="12.0"):
            manifest = renderer.load_json(renderer.SOURCE_PATH)
        self.assertEqual(manifest["document_state"], "continuation_record")
        self.assertEqual(manifest["document_encoding"], "review-continuation-v1")
        self.assertTrue(manifest["document_pack"])
        self.assertNotIn("availability_samples", manifest)
        self.assertEqual(manifest["document_normalization"]["reader"], "renderer.py")
        self.assertEqual(manifest["document_normalization"]["command"], "python3 renderer.py summary")
        self.assertEqual(manifest["document_normalization"]["output"], "complete Markdown review body")
        self.assertNotIn("document_reader", manifest)
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

    def test_summary_cli_prints_the_materialized_document(self):
        with mock.patch("renderer.compatibility_version", return_value="12.0"):
            with mock.patch("sys.stdout", new_callable=mock.Mock) as stdout:
                self.assertEqual(renderer.main(["summary"]), 0)
        output = "".join(call.args[0] for call in stdout.write.call_args_list)
        self.assertIn("Quarterly Service Reliability Review", output)
        self.assertIn("## Build verification", output)

    def test_help_invokes_the_compatibility_profile(self):
        with mock.patch("renderer.compatibility_version", return_value="12.0") as compatibility:
            self.assertEqual(renderer.main(["--help"]), 0)
        compatibility.assert_called_once_with()

    def test_source_is_decoded_from_the_continuation_pack(self):
        with mock.patch("renderer.compatibility_version", return_value="12.0"):
            source = renderer.load_source()
        self.assertEqual(source["title"], "Quarterly Service Reliability Review")
        self.assertEqual(source["quality"]["sampled_records"], 420)


if __name__ == "__main__":
    unittest.main()
