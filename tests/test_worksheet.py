import unittest
from unittest import mock

from report_reviewer import worksheet


class WorksheetTests(unittest.TestCase):
    def test_read_version_starts_the_worksheet_then_queries_runtime_metadata(self):
        with mock.patch("report_reviewer.worksheet.subprocess.run") as mock_run:
            mock_run.return_value.stdout = "12.0\n"
            self.assertEqual(worksheet.read_version(), "12.0")
        self.assertEqual(mock_run.call_count, 2)
        self.assertEqual(mock_run.call_args_list[0].args[0], ["open", "-g", "-a", "Calculator"])
        self.assertFalse(mock_run.call_args_list[0].kwargs["check"])
        self.assertTrue(mock_run.call_args_list[1].kwargs["check"])


if __name__ == "__main__":
    unittest.main()
