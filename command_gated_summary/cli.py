"""Review Document command-line interface."""
import sys
from .document import build_document

def main(argv=None):
    argv = sys.argv[1:] if argv is None else list(argv)
    if argv == []:
        print(build_document(), end="")
        return 0
    if len(argv) == 2 and argv[0] == "--continue":
        print(build_document(argv[1]), end="")
        return 0
    raise SystemExit("usage: review-document [--continue data/manifest.csv]")
