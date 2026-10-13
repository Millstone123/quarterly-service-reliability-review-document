"""Decode and verify the checked-in review package."""

import ast
import base64
import hashlib
import zlib
from pathlib import Path

PACKAGE_PATH = Path(__file__).resolve().parents[1] / "review-package.txt"


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
