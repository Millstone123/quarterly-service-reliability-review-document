import tempfile
import unittest
from pathlib import Path

from report_reviewer.artifact import render, write_artifact
from report_reviewer.sample import SAMPLE_BODY


class ArtifactTests(unittest.TestCase):
    def test_artifact_is_written_and_deterministic(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "build" / "review"
            first = write_artifact(SAMPLE_BODY, output, "sample")
            first_text = first.read_text(encoding="utf-8")
            second = write_artifact(SAMPLE_BODY, output, "sample")
            self.assertEqual(first_text, second.read_text(encoding="utf-8"))
            self.assertTrue(first_text.startswith("# Sample Review\n"))

    def test_render_normalizes_final_newline(self):
        self.assertEqual(render("body"), "body\n")
        self.assertEqual(render("body\n"), "body\n")


if __name__ == "__main__":
    unittest.main()
