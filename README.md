# Quarterly Service Reliability Review

This project materializes a quarterly service review from checked-in worksheet observations.

## Build the complete review

`preview.md` contains the opening section. The complete review is assembled by the repository workflow:

```sh
./summary
```

The workflow runs the tests, assembles the review sections, performs the live worksheet application compatibility check, verifies the finalized body against `data/index.json`, and writes `build/review/review_report.md`.

## Tests

```sh
make test
```
