"""Read checked-in terminal report rows."""
import csv
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Row:
    row: str
    source: str
    value: str

def load_rows(path):
    with Path(path).open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError("manifest must contain rows")
    return [Row(item["row"], item["source"], item["value"]) for item in rows]
