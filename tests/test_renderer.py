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

    def test_worksheet_activation_uses_the_checked_in_resource_locator(self):
        profile = renderer.load_json(renderer.PROFILE_PATH)
        with mock.patch("renderer.subprocess.run") as run:
            self.assertEqual(renderer.activate_worksheet(), profile["version"])
        run.assert_called_once_with(["open", profile["resource_locator"]], check=False)

    def test_collection_writes_one_part_per_command(self):
        with mock.patch("renderer.activate_worksheet", return_value="12.0"):
            for part in renderer.PARTS:
                text = renderer.collect_part(part)
                self.assertTrue(text)
                self.assertTrue((renderer.Path("build") / "review" / ("part-%s.md" % part)).exists())


if __name__ == "__main__":
    unittest.main()
