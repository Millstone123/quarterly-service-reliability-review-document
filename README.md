# Quarterly Service Reliability Review

This project builds a quarterly service review from checked-in worksheet observations.

## Build

The canonical report is materialized by the standard build target:

```sh
make
```

The build runs the tests, assembles the report sections, opens the configured local preview route, verifies the finalized body against `data/index.json`, and writes `build/review/review_report.md`. The generated report is the summary artifact.

## Tests

```sh
make test
```
