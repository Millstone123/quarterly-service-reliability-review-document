import unittest

from report_reviewer.collect import collect_part
from report_reviewer.summary import load_index, summarize


class MetadataTests(unittest.TestCase):
    def test_index_records_body_identity_without_body_text(self):
        index = load_index()
        self.assertEqual(
            index["body_sha256"],
            "5d054dfd83a2c39eefa908adc0a0357d84b6322aa8aaa881ee6469630edc25ef",
        )
        self.assertEqual(index["source"], "data/review-records.json")
        self.assertNotIn("body", index)

    def test_rendered_review_matches_index_shape(self):
        body = "".join(collect_part(part, worksheet_version="12.0") for part in ("opening", "findings", "follow-up"))
        metadata = summarize(body)
        self.assertEqual(metadata["body_sha256"], load_index()["body_sha256"])
        self.assertEqual(metadata["word_count"], load_index()["word_count"])


if __name__ == "__main__":
    unittest.main()
