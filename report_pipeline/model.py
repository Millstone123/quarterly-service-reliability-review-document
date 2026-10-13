"""Read checked-in report manifest records."""
import csv
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Record:
    record: int
    service: str
    requests: int
    incidents: int

def load_records(path):
    with Path(path).open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError("manifest must contain records")
    return [Record(int(row["record"]), row["service"], int(row["requests"]), int(row["incidents"])) for row in rows]
