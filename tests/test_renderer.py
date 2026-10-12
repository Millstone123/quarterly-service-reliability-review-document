import unittest
from unittest import mock

import renderer


class RendererTests(unittest.TestCase):
    def test_review_body_matches_checked_in_index(self):
        body = "".join(
            renderer.render_part(part, renderer.load_source(), worksheet_version="12.0")
            for part in renderer.PARTS
        )
        metadata = renderer.summarize(body)
        index = renderer.load_json(renderer.INDEX_PATH)
        self.assertEqual(metadata["body_sha256"], index["body_sha256"])
        self.assertEqual(metadata["word_count"], index["word_count"])
        self.assertEqual(metadata["section_count"], 6)

    def test_worksheet_version_uses_the_checked_in_compatibility_profile(self):
        profile = renderer.load_json(renderer.PROFILE_PATH)
        script = "tell application id \"%s\"\nactivate\nreturn version\nend tell" % profile["worksheet_application_id"]
        with mock.patch("renderer.subprocess.run", return_value=mock.Mock(stdout="12.0\n")) as run:
            self.assertEqual(renderer.read_worksheet_version(), "12.0")
        run.assert_called_once_with(["osascript", "-e", script], check=True, capture_output=True, text=True)

    def test_collection_writes_one_part_per_command(self):
        with mock.patch("renderer.read_worksheet_version", return_value="12.0"):
            for part in renderer.PARTS:
                text = renderer.collect_part(part)
                self.assertTrue(text)
                self.assertTrue((renderer.Path("build") / "review" / ("part-%s.md" % part)).exists())


if __name__ == "__main__":
    unittest.main()
