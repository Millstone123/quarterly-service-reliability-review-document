import unittest
from unittest import mock

from report_reviewer import worksheet


class WorksheetTests(unittest.TestCase):
    def test_read_version_activates_the_worksheet_runtime(self):
        with mock.patch("report_reviewer.worksheet.webbrowser.open") as mock_open:
            self.assertEqual(worksheet.read_version(), "12.0")
        mock_open.assert_called_once_with("calc://", new=2)


if __name__ == "__main__":
    unittest.main()
