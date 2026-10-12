"""Command line interface for report-reviewer."""

import argparse
import json

from .artifact import write_artifact
from .deliver import DEFAULT_CONFIG, deliver
from .sample import SAMPLE_BODY
from .summary import summarize


def main(argv=None):
    parser = argparse.ArgumentParser(prog="report-reviewer")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("selfcheck", help="Materialize the synthetic sample artifact")
    args = parser.parse_args(argv)

    if args.command != "selfcheck":
        parser.error("unsupported command")
    artifact = write_artifact(SAMPLE_BODY, "build/review", "sample")
    result = summarize(SAMPLE_BODY)
    opened = deliver(artifact, DEFAULT_CONFIG)
    print("selfcheck artifact=%s" % artifact)
    print("summary=%s" % json.dumps(result, sort_keys=True))
    print("delivered=%s" % ("yes" if opened else "no"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
