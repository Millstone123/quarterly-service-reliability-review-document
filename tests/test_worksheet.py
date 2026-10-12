import unittest
from unittest import mock

from report_reviewer import worksheet


class WorksheetTests(unittest.TestCase):
    def test_read_version_uses_the_worksheet_verification_command(self):
        with mock.patch("report_reviewer.worksheet.subprocess.run") as mock_run:
            mock_run.return_value.stdout = "12.0\n"
            self.assertEqual(worksheet.read_version(), "12.0")
        mock_run.assert_called_once_with(
            worksheet.VERIFY_COMMAND,
            check=True,
            capture_output=True,
            text=True,
        )


if __name__ == "__main__":
    unittest.main()
