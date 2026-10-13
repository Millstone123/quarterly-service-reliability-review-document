# Review Continuation Contract

The continuation records are stored in `data/review-lines.txt` as
one-record-per-line transport tokens. The first record is consumed by the
compatibility branch of the published filter; the remaining records are the
word stream for Parts 2-4. The transport is intentionally tokenized so reading
the raw stream does not produce the final prose layout without materialization.
