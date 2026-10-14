"""Command-line entry point for service reliability reviews."""

from __future__ import annotations

import argparse

from .report import fields, render


def main(argv=None):
    parser = argparse.ArgumentParser(description="Generate a service reliability review.")
    parser.add_argument("--summary", action="store_true", help="print the complete review summary")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    args = parser.parse_args(argv)
    if args.format == "json":
        import json

        print(json.dumps(fields(), indent=2, sort_keys=True))
    else:
        print(render(), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
