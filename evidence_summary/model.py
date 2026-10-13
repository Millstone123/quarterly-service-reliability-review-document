"""Read checked-in evidence manifest records."""
import csv
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Evidence:
    section: str
    source: str
    record: int

def load_evidence(path):
    with Path(path).open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError("manifest must contain evidence")
    return [Evidence(row["section"], row["source"], int(row["record"])) for row in rows]
