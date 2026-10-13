"""Command-line entry point for the checked-in review document."""

from runtime.compatibility import compatibility_version
from runtime.package import load_package, read_document, verify
from runtime.workflow import main


if __name__ == "__main__":
    raise SystemExit(main())
