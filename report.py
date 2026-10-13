#!/usr/bin/env python3
"""Render the canonical review document from tracked text records."""
from pathlib import Path
import csv
import math

ROOT = Path(__file__).resolve().parent
MEASUREMENTS = ROOT / "data" / "measurements.csv"


def fields():
    """Return review measurements derived from the tracked request samples."""
    with MEASUREMENTS.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    latencies = sorted(int(row["latency_ms"]) for row in rows)
    failed = sum(int(row["status"]) >= 400 for row in rows)
    total = len(rows)
    p95 = latencies[max(0, math.ceil(0.95 * total) - 1)]
    failed_share = failed / total
    availability = 1.0 - failed_share
    decision = "go" if p95 <= 250 and failed_share <= 0.01 else "hold"
    return {
        "p95_latency_ms": p95,
        "failed_request_share": f"{failed_share:.4f}",
        "availability": f"{availability:.4f}",
        "release_decision": decision,
        "request_count": total,
    }


def render():
    """Render the complete review document."""
    data = fields()
    return (
        "# Service Reliability Review\n"
        "## Release Measurements\n"
        f"p95_latency_ms={data['p95_latency_ms']}\n"
        f"failed_request_share={data['failed_request_share']}\n"
        f"availability={data['availability']}\n\n"
        "## Closing Recommendation\n"
        f"release_decision={data['release_decision']}\n"
        f"request_count={data['request_count']}\n"
    )


if __name__ == "__main__":
    print(render(), end="")
