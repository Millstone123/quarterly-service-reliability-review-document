import unittest
from pathlib import Path

from service_reliability_report.model import load_services
from service_reliability_report.report import build_report


class ReliabilityReportTests(unittest.TestCase):
    def test_report_has_deterministic_totals(self):
        observations = load_services(Path("data/services.csv"))
        report = build_report(observations)
        self.assertIn("services=4", report)
        self.assertIn("incidents=4", report)
        self.assertIn("affected_requests=1779", report)
        self.assertIn("highest_impact_service=export", report)

    def test_empty_report_is_rejected(self):
        with self.assertRaises(ValueError):
            build_report([])


if __name__ == "__main__":
    unittest.main()
