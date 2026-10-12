# Quarterly Service Reliability Review

This repository generates a quarterly review from checked-in worksheet observations.

## Build

The review document is a generated artifact and is not checked in. Materialize the current document with the standard build target:

```sh
make
```

The build runs the tests, assembles the report sections, opens the configured local preview, verifies the finalized body against `data/index.json`, and writes `build/review/review_report.md`.

## Tests

```sh
make test
```
