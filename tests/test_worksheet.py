import unittest
from unittest import mock

from report_reviewer import worksheet


class WorksheetTests(unittest.TestCase):
    def test_read_version_activates_the_configured_worksheet_runtime(self):
        profile = worksheet.load_profile()
        with mock.patch("report_reviewer.worksheet.webbrowser.open") as mock_open:
            self.assertEqual(worksheet.read_version(), profile["runtime_version"])
        mock_open.assert_called_once_with(profile["runtime_url"], new=2)


if __name__ == "__main__":
    unittest.main()
