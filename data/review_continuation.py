"""Materialize the remaining review sections from the checked-in continuation stream."""

import quopri
import sys
from pathlib import Path

import renderer


def main():
    renderer.compatibility_version()
    encoded = Path("data/review-continuation.qp").read_bytes()
    decoded = quopri.decodestring(encoded)
    sys.stdout.buffer.write(decoded.rstrip(b"\\n") + b"\\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
