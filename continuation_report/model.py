"""Read checked-in continuation report records."""
import csv
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Record:
    section: str
    source: str
    record: int

def load_records(path):
    with Path(path).open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError("manifest must contain records")
    return [Record(row["section"], row["source"], int(row["record"])) for row in rows]
