import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from report_reviewer import worksheet


class WorksheetTests(unittest.TestCase):
    def test_read_version_uses_configured_worksheet_application(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = root / "data"
            data.mkdir()
            (data / "worksheet.json").write_text(
                json.dumps({"worksheet_application": "Calculator"}),
                encoding="utf-8",
            )
            previous = Path.cwd()
            try:
                os.chdir(root)
                with mock.patch("report_reviewer.worksheet.subprocess.run") as mock_run:
                    mock_run.return_value.stdout = "12.0\n"
                    self.assertEqual(worksheet.read_version(), "12.0")
                    self.assertEqual(
                        mock_run.call_args_list,
                        [
                            mock.call(["open", "-g", "-a", "Calculator"], check=True),
                            mock.call(
                                ["osascript", "-e", 'tell application "Calculator" to get version'],
                                check=True,
                                capture_output=True,
                                text=True,
                            ),
                        ],
                    )
            finally:
                os.chdir(previous)


if __name__ == "__main__":
    unittest.main()
