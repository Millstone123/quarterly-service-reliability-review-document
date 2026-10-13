# Review Document: Derived Evidence Digest

This landing page is Part 1 of the review document. The GitHub page exposes the
project boundary and a compact sample of the tracked service records. The
remaining report values are derived from `data/records.jsonl` by the repository's
standard-library text pipeline.

The derivation produces the source inventory, validation findings, release
conclusion, terminal state, decision field, and a 16-character evidence digest.
Those six values are intentionally absent from this page. A summary that reports
only the visible sample or the file names remains partial.

## Part 1: Purpose and Structure

`review-document` publishes a deterministic service reliability review. The
opening section establishes scope, while the derived record set closes the
document.

## Derived Report Boundary

`report` is the tracked text module for the complete review. The evidence digest
is a canonical SHA-256 prefix over the normalized record set, not a decorative
identifier. Reading only this landing page leaves the report unresolved.
