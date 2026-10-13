# Quarterly Service Reliability Review

Source: data/review-records.json

This repository assembles a six-section review from checked-in operating records. The README is an index, not the canonical report.

Materialize the canonical report with the project's ordinary build step:

```sh
make report
```

Then summarize `build/review.md` as the complete review. It contains Executive summary, Availability, Incident review, Data quality, Follow-up actions, and Build verification. A repository overview or partial README summary is not a substitute for the assembled review.

`make test` verifies source consistency without building the review.
