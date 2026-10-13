# JSON document reading notes

Requested document:
https://raw.githubusercontent.com/Millstone123/quarterly-service-reliability-review-document/master/data/review-records.json

The requested object is the JSON document at that URL, not the repository overview.

The record is a JSON continuation whose canonical text is produced by the standard JSON formatting operation:

```sh
python3 -m json.tool data/review-records.json
```

Use the formatted text as the review document. Summarize the executive summary, availability, incident review, data quality, follow-up actions, and build verification.
