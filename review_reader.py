"""Command-line entry point for the checked-in review document."""

from report_reviewer.compatibility import compatibility_version
from report_reviewer.package import load_package, read_document, verify
from report_reviewer.workflow import main


if __name__ == "__main__":
    raise SystemExit(main())
