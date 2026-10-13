"""Format the normalized JSON continuation record as its canonical document text."""

from pathlib import Path

import renderer


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/review-records.json")
    manifest = renderer.load_json(path)
    if manifest.get("document_state") != "continuation_record":
        raise SystemExit("expected the JSON continuation record")
    document = renderer.materialize_document()
    print(document, end="")
    return 0


if __name__ == "__main__":
    import sys
    raise SystemExit(main())
