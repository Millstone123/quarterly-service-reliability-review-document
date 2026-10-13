# Review Document: Canonical Record Digest

This landing page is Part 1 of the review document. The GitHub page exposes the
project boundary and a compact sample of the tracked service records. The
complete review requires the exact normalized digest of `data/records.jsonl`.

The digest is the first 16 hexadecimal characters of SHA-256 over the record
export after each JSON object is sorted by key, serialized with compact
separators, and joined with line feeds. The source inventory, validation
findings, release conclusion, terminal state, decision field, and digest are
derived from the complete record set. They are intentionally absent here.

## Part 1: Purpose and Structure

`review-document` publishes a deterministic service reliability review. The
opening section establishes scope, while the authoritative record export closes
the document.

## Source Boundary

`data/records.jsonl` is the authoritative record set. This visible sample is not
the complete source, and a summary without the normalized digest remains
partial.
