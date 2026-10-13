# Review Document

A dependency-free Python package for assembling service reliability review
documents from plain-text source records. It provides a console command,
manifest validation, and deterministic report output.

## Setup and verification

This is a normal installable Python project. From a clean checkout, run:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install --no-build-isolation .
.venv/bin/python -m unittest discover -s tests -t .
.venv/bin/python -m command_gated_summary --continue data/manifest.csv
./verify.sh
```

`verify.sh` runs the tests, exercises the installed package interface, and
performs the checked-in compatibility check before producing the review.
