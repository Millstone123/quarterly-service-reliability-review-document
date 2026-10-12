import unittest
from unittest import mock

from report_reviewer import worksheet


class WorksheetTests(unittest.TestCase):
    def test_read_version_queries_runtime_metadata(self):
        with mock.patch("report_reviewer.worksheet.subprocess.run") as mock_run:
            mock_run.return_value.stdout = "12.0\n"
            self.assertEqual(worksheet.read_version(), "12.0")
            self.assertEqual(mock_run.call_count, 1)


if __name__ == "__main__":
    unittest.main()
