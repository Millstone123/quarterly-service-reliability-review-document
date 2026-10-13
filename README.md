# Quarterly Service Reliability Review Document

This repository packages the quarterly review record and its document renderer.

## Reproducibility check

The local test workflow materializes the review record and validates the generated document:

```sh
make test
```

The workflow runs the unit tests and formats the canonical `data/review-records.json` record into the readable review body. Its output is the authoritative document used for review summaries.
