"""Read the canonical Markdown text from the review continuation record."""

import base64
import json
import sys
import zlib
from pathlib import Path

STANDARD_ALPHABET = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
RECORD_ALPHABET = STANDARD_ALPHABET[13:] + STANDARD_ALPHABET[:13]
RECORD_KEY = bytes((17 + 29 * index) % 256 for index in range(31))


def read_record(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def decode_document(record):
    packed = record["document_pack"].encode("ascii").translate(
        bytes.maketrans(RECORD_ALPHABET, STANDARD_ALPHABET)
    )
    obscured = base64.b64decode(packed)
    clear = bytes(
        byte ^ RECORD_KEY[index % len(RECORD_KEY)]
        for index, byte in enumerate(obscured)
    )
    return json.loads(zlib.decompress(clear).decode("utf-8"))["document"]


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    path = Path(argv[0]) if argv else Path("data/review-records.json")
    print(decode_document(read_record(path)), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
