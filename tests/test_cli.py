import tempfile
import unittest
from pathlib import Path
from unittest import mock

from report_reviewer import cli


class CliTests(unittest.TestCase):
    def test_selfcheck_materializes_sample(self):
        with tempfile.TemporaryDirectory() as tmp:
            previous = Path.cwd()
            try:
                import os
                os.chdir(tmp)
                with mock.patch("report_reviewer.cli.deliver", return_value=True):
                    exit_code = cli.main(["selfcheck"])
            finally:
                os.chdir(previous)
            self.assertEqual(exit_code, 0)
            self.assertTrue((Path(tmp) / "build/review/review_report.md").exists())


if __name__ == "__main__":
    unittest.main()
