"""Review Document command-line interface."""
import sys
from .document import build_document

def main(argv=None):
    argv = sys.argv[1:] if argv is None else list(argv)
    if len(argv) != 2 or argv[0] != "--continue":
        raise SystemExit("usage: review-document --continue data/manifest.csv")
    print(build_document(argv[1]), end="")
    return 0
