# Review Continuation Contract

The continuation records are stored in `data/review-lines.txt` as
one-record-per-line transport tokens. `data/compress-filter.txt` is the local
archive adapter used only to validate the transport before the stored words
are materialized. The transport is intentionally tokenized so reading the raw
stream does not produce the final prose layout without materialization.
