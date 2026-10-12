# Quarterly Service Reliability Review

This project assembles a quarterly service review from raw worksheet observations.

## Complete review

`preview.md` contains the document opening and executive summary. The remaining review sections, including live worksheet verification, are calculated from the raw observations and materialized by the repository workflow:

```sh
./summary
```

The command writes `build/review/review_report.md`, verifies the finalized body against `data/index.json`, and records live worksheet compatibility metadata so the numeric results can be checked against the worksheet environment.

## Tests

```sh
make test
```
