"""Command-gated summary CLI."""
import sys
from .compatibility import compatibility_version
from .model import load_fields
from .report import render

def main(argv=None):
    argv = sys.argv[1:] if argv is None else list(argv)
    if len(argv) != 2 or argv[0] != "--continue":
        raise SystemExit("usage: python3 -m command_gated_summary --continue data/manifest.csv")
    compatibility_version()
    print(render(load_fields(argv[1])), end="")
    return 0
