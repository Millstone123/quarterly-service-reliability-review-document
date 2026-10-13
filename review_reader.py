"""Read the canonical review package."""

import base64
import sys
import zlib
from pathlib import Path
from zipfile import ZipFile

ARCHIVE = Path(__file__).with_name("review-package.zip")


def read_document():
    with ZipFile(ARCHIVE) as package:
        packed = package.read("review.dat")
    return zlib.decompress(base64.b64decode(packed)).decode("utf-8")


def verify():
    import ast
    body = read_document()
    with ZipFile(ARCHIVE) as package:
        expected = ast.literal_eval(package.read("verification.json").decode("utf-8"))
    import hashlib
    actual = hashlib.sha256(body.encode("utf-8")).hexdigest()
    if actual != expected["document_sha256"] or len(body.encode("utf-8")) != expected["document_bytes"]:
        raise ValueError("review package verification failed")
    return expected


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    sys.path.insert(0, str(ARCHIVE))
    import compatibility
    compatibility.compatibility_version()
    if argv == ["--verify"]:
        verify()
        print("review_package=verified")
        return 0
    if argv:
        raise SystemExit("usage: review_reader.py [--verify]")
    print(read_document(), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
