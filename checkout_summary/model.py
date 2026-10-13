"""Read checked-in checkout summary fields."""
import csv
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Field:
    field: str
    source: str
    value: str

def load_fields(path):
    with Path(path).open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError("manifest must contain fields")
    return [Field(item["field"], item["source"], item["value"]) for item in rows]
