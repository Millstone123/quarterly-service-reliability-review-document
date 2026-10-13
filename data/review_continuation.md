# Review Continuation Contract

The continuation records are stored in `data/review-records.json` as structured
JSON fields. `python3 -m json.tool` is the standard-library formatter used to
materialize the stored fields before the final prose layout. The transport is
intentionally structured so reading the landing page does not produce the final
prose layout without formatting.
