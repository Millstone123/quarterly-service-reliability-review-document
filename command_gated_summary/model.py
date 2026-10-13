"""Read the distributed review inputs from checked-in or packaged text."""
import csv
from dataclasses import dataclass
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = PACKAGE_ROOT.parent
INPUTS = PACKAGE_ROOT / "data" / "inputs"
if not INPUTS.exists():
    INPUTS = PROJECT_ROOT / "data" / "inputs"

@dataclass(frozen=True)
class ReviewInput:
    name: str
    text: str

def load_fields(path):
    with Path(path).open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError("manifest must contain fields")
    return [ReviewInput(item["field"], item["value"]) for item in rows]

def load_review_inputs():
    paths = sorted(INPUTS.glob("*.txt"))
    if not paths:
        raise ValueError("distributed review inputs are required")
    return [ReviewInput(path.stem, path.read_text(encoding="utf-8").strip()) for path in paths]
