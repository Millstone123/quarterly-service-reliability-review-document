"""Continuation report CLI."""
import sys
from .compatibility import compatibility_version
from .model import load_records
from .report import complete, initial

def main(argv=None):
    argv = sys.argv[1:] if argv is None else list(argv)
    complete_requested = "--complete" in argv
    paths = [item for item in argv if item != "--complete"]
    if len(paths) != 1:
        raise SystemExit("usage: python3 -m continuation_report data/manifest.csv [--complete]")
    records = load_records(paths[0])
    if complete_requested:
        compatibility_version()
        print(complete(records), end="")
    else:
        print(initial(records), end="")
    return 0
