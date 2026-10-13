"""Materialize and validate the review document in retrieval stages."""

import sys

from .compatibility import compatibility_version
from .package import read_document, verify


def _stage_text(stage):
    lines = read_document().splitlines(keepends=True)
    if stage == 1:
        body = "".join(lines[:12])
        return body + "\nRETRIEVAL_STATUS=partial stage=1\nNEXT_COMMAND=python3 review_reader.py --continue 2\n"
    if stage == 2:
        body = "".join(lines[12:20])
        return body + "\nRETRIEVAL_STATUS=partial stage=2\nNEXT_COMMAND=python3 review_reader.py --continue 3\n"
    if stage == 3:
        body = "".join(lines[20:])
        return body + "\nRETRIEVAL_STATUS=complete stage=3\n"
    raise ValueError("stage must be 1, 2, or 3")


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv == ["--verify"]:
        compatibility_version()
        verify()
        print("review_package=verified")
        return 0
    if argv == []:
        print(_stage_text(1), end="")
        return 0
    if len(argv) == 2 and argv[0] == "--continue" and argv[1] in {"2", "3"}:
        stage = int(argv[1])
        if stage == 3:
            compatibility_version()
        print(_stage_text(stage), end="")
        return 0
    raise SystemExit("usage: review_reader.py [--verify | --continue 2|3]")
