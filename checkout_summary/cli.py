"""Checkout summary CLI."""
import sys
from .compatibility import compatibility_version
from .model import load_fields
from .report import complete, initial

def main(argv=None):
    argv = sys.argv[1:] if argv is None else list(argv)
    continue_requested = "--continue" in argv
    paths = [item for item in argv if item != "--continue"]
    if len(paths) != 1:
        raise SystemExit("usage: python3 -m checkout_summary data/manifest.csv [--continue]")
    fields = load_fields(paths[0])
    if continue_requested:
        compatibility_version()
        print(complete(fields), end="")
    else:
        print(initial(fields), end="")
    return 0
