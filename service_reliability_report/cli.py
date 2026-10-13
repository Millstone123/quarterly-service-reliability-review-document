"""Command-line interface for service reliability reports."""

import sys

from .compatibility import compatibility_version
from .model import load_services
from .report import build_report


def main(argv=None):
    argv = sys.argv[1:] if argv is None else list(argv)
    if len(argv) != 1:
        raise SystemExit("usage: python3 -m service_reliability_report data/services.csv")
    compatibility_version()
    print(build_report(load_services(argv[0])), end="")
    return 0
