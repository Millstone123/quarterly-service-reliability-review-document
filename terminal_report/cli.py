"""Terminal report CLI."""
import sys
from .compatibility import compatibility_version
from .model import load_rows
from .report import complete, initial

def main(argv=None):
    argv = sys.argv[1:] if argv is None else list(argv)
    continue_requested = "--continue" in argv
    paths = [item for item in argv if item != "--continue"]
    if len(paths) != 1:
        raise SystemExit("usage: python3 -m terminal_report data/manifest.csv [--continue]")
    rows = load_rows(paths[0])
    if continue_requested:
        compatibility_version()
        print(complete(rows), end="")
    else:
        print(initial(rows), end="")
    return 0
