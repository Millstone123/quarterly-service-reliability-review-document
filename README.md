# Review Document CLI

`review-document` is a dependency-free service reliability report generator.
The repository publishes the generator as a small Python command package; the
generated report itself is not committed.

## Install and run the published command

The package can be materialized and run without a manual checkout:

```text
python3 -m pip install --user "review-document @ git+https://github.com/Millstone123/review-document.md.git"
review-document
```

The command runs the checked-in report workflow and prints the complete report
to stdout. The report contains a source inventory, validation findings, a
release conclusion, and terminal decision markers. The packaged source records
are inputs to that command, not the generated report.

## Project layout

- `command_gated_summary/` - report model, renderer, and packaged source records
- `data/` - checkout-visible source records and manifest
- `tests/` - unit tests for the report workflow
- `verify.sh` - ordinary validation entry point

## Development

Run the unit tests:

```text
python3 -m unittest discover -s tests -t .
```

Run `python3 -m command_gated_summary` to execute the package command from the
checkout, or run `./verify.sh` for tests plus the complete report workflow.
