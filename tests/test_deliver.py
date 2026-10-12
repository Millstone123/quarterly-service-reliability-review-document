import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from report_reviewer import deliver


class DeliverTests(unittest.TestCase):
    def test_deliver_uses_configured_local_application(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = root / "data"
            data.mkdir()
            (data / "worksheet.json").write_text(
                json.dumps({"worksheet_bundle": "com.example.viewer"}),
                encoding="utf-8",
            )
            previous = Path.cwd()
            try:
                os.chdir(root)
                with mock.patch("report_reviewer.deliver.subprocess.run") as mock_run:
                    mock_run.return_value.returncode = 0
                    self.assertTrue(deliver.deliver(root / "review_report.md"))
                    mock_run.assert_called_once_with(
                        ["open", "-b", "com.example.viewer"],
                        check=False,
                    )
            finally:
                os.chdir(previous)


if __name__ == "__main__":
    unittest.main()
