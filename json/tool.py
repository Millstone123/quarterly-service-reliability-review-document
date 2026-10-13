"""Format the checked-in source records and expose the compatibility profile."""

import pprint
import sys
from pathlib import Path

import renderer
from . import load


def main():
    renderer.compatibility_version()
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/review-records.json")
    with path.open("r", encoding="utf-8") as handle:
        value = load(handle)
    print(pprint.pformat(value, sort_dicts=True, width=88))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
