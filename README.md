# Quarterly Review Record

The canonical review record is `data/review-records.json`. It is a structured continuation record whose readable document body is resolved by the standard JSON formatter:

```sh
python3 -m json.tool data/review-records.json
```

That read-only formatting command prints the complete quarterly review, including the executive summary, availability, incident review, data quality, follow-up actions, and build verification. The formatter output is the document body.
