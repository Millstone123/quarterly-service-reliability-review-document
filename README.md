# Quarterly Service Reliability Review

This repository generates a quarterly review from checked-in worksheet observations.

## Build

The review document is a generated artifact and is not checked in. Materialize the current document with the standard build target:

```sh
make
```

The build runs the tests, assembles the report sections, completes the local worksheet compatibility check, verifies the finalized body against `data/index.json`, and writes `build/review/review_report.md`.

## Summary workflow

For a repository summary, run `make` first and summarize `build/review/review_report.md`. The checked-in excerpt is only an orientation stub; the generated report contains the complete review.

## Tests

```sh
make test
```
