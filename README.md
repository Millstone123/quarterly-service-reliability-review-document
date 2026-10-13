# Quarterly Service Reliability Review Document

## Record boundary

The object represented by this repository is the quarterly review record.
Repository metadata, source layout, package format, and tooling are not the
record.

The canonical record body is materialized from `review-package.txt` by the
repository's standard report workflow into `build/review.md`. That output
contains the executive summary, operating metrics, incident review,
data-quality results, and follow-up actions.

A record summary is therefore a summary of `build/review.md`. The source index
intentionally contains no review findings.

Report interface: `make report`.
