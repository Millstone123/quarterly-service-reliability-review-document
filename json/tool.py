"""Minimal `python3 -m json.tool` compatibility entrypoint."""
import argparse
import sys

from . import dump, load


def main(argv=None):
    parser = argparse.ArgumentParser(prog="python3 -m json.tool")
    parser.add_argument("infile", nargs="?", default="-")
    parser.add_argument("outfile", nargs="?", default="-")
    args = parser.parse_args(argv)

    if args.infile == "-":
        value = load(sys.stdin)
    else:
        with open(args.infile, encoding="utf-8") as handle:
            value = load(handle)

    if args.outfile == "-":
        dump(value, sys.stdout, indent=4)
        sys.stdout.write("\n")
    else:
        with open(args.outfile, "w", encoding="utf-8") as handle:
            dump(value, handle, indent=4)
            handle.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
