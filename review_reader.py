"""Read the canonical encoded review package."""

import ast
import base64
import hashlib
import sys
import zlib
from pathlib import Path

PACKAGE_PATH = Path(__file__).with_name("review-package.txt")


def load_package():
    packed = "".join(PACKAGE_PATH.read_text(encoding="ascii").split())
    return ast.literal_eval(zlib.decompress(base64.b64decode(packed)).decode("utf-8"))


def read_document():
    return load_package()["entries"]["review.md"]


def verify():
    package = load_package()
    expected = ast.literal_eval(package["entries"]["verification.json"])
    body = read_document().encode("utf-8")
    actual = hashlib.sha256(body).hexdigest()
    if actual != expected["document_sha256"] or len(body) != expected["document_bytes"]:
        raise ValueError("review package verification failed")
    return expected


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    package = load_package()
    namespace = {"__name__": "review_package_compatibility"}
    exec(compile(package["entries"]["compatibility.py"], "review-package.txt:compatibility.py", "exec"), namespace)
    namespace["compatibility_version"]()
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
