# Quarterly Service Reliability Review

Source: data/review-records.json

The repository stores the canonical operating records as reviewable JSON. Inspect the normalized source with the standard formatter:

```sh
python3 -m json.tool data/review-records.json
```

Use that record set to summarize the quarterly review. `make report` assembles the same source into `build/review.md`; `make test` verifies source consistency without running the formatter.
