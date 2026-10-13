"""Evidence summary CLI."""
import sys
from .compatibility import compatibility_version
from .model import load_evidence
from .summary import render

def main(argv=None):
    argv = sys.argv[1:] if argv is None else list(argv)
    if len(argv) != 1:
        raise SystemExit("usage: python3 -m evidence_summary data/manifest.csv")
    compatibility_version()
    print(render(load_evidence(argv[0])), end="")
    return 0
