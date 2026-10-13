"""Materialize and validate the review document."""

import sys

from .compatibility import compatibility_version
from .package import read_document, verify


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    compatibility_version()
    if argv == ["--verify"]:
        verify()
        print("review_package=verified")
        return 0
    if argv:
        raise SystemExit("usage: review_reader.py [--verify]")
    print(read_document(), end="")
    return 0
