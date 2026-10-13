"""Report-pipeline CLI."""
import sys
from .compatibility import compatibility_version
from .model import load_records
from .report import generate

def main(argv=None):
    argv = sys.argv[1:] if argv is None else list(argv)
    if len(argv) != 1:
        raise SystemExit("usage: python3 -m report_pipeline data/manifest.csv")
    compatibility_version()
    print(generate(load_records(argv[0])), end="")
    return 0
