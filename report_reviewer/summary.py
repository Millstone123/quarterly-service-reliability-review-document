"""Load and summarize a finalized review body."""

import hashlib
import json
import re
from pathlib import Path

DEFAULT_INDEX = Path("data") / "index.json"


def load_index(path=DEFAULT_INDEX):
    """Return the repository integrity index."""
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def summarize(body):
    """Return stable identity and structure metadata for a review body."""
    sections = re.findall(r"^## (.+)$", body, flags=re.MULTILINE)
    return {
        "body_sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
        "section_count": len(sections),
        "sections": sections,
        "word_count": len(body.split()),
    }
