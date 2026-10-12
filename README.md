# Quarterly Service Reliability Review

This project assembles a quarterly service review from raw worksheet observations.

## Complete review

`preview.md` contains the document opening. The remaining sections are calculated from the raw observations and are materialized by the repository workflow:

```sh
./summary
```

The command writes `build/review/review_report.md`, verifies the finalized report, and then opens the configured worksheet bundle once for live numeric review.

## Tests

```sh
make test
```
