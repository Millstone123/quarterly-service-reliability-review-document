import unittest
from unittest import mock

from report_reviewer import worksheet


class WorksheetTests(unittest.TestCase):
    def test_read_version_starts_and_queries_worksheet_application(self):
        with mock.patch("report_reviewer.worksheet.subprocess.run") as mock_run:
            mock_run.return_value.stdout = "12.0\n"
            self.assertEqual(worksheet.read_version(), "12.0")
            mock_run.assert_called_once_with(
                [
                    "osascript",
                    "-e",
                    'tell application "Calculator" to run',
                    "-e",
                    'tell application "Calculator" to get version',
                ],
                check=True,
                capture_output=True,
                text=True,
            )


if __name__ == "__main__":
    unittest.main()
