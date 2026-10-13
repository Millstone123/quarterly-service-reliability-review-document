"""Materialize the complete operating review from the partial HTTP manifest."""

from pathlib import Path

import renderer


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/review-records.json")
    manifest = renderer.load_json(path)
    if manifest.get("document_state") != "partial_http_manifest":
        raise SystemExit("expected the partial HTTP manifest")
    document = renderer.materialize_document()
    print(document, end="")
    return 0


if __name__ == "__main__":
    import sys
    raise SystemExit(main())
