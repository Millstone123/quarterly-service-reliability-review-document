import unittest
from pathlib import Path

from service_reliability_report.model import load_services


class ServiceDataTests(unittest.TestCase):
    def test_fixture_is_reviewable_text(self):
        text = Path("data/services.csv").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("service,availability,incidents,affected_requests"))
        self.assertEqual(len(load_services("data/services.csv")), 4)


if __name__ == "__main__":
    unittest.main()
