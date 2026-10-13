# Review Document: Encoded Appendix

This landing page is Part 1 of the review document. The GitHub page and raw
text view intentionally expose only the opening section. The remaining report
is stored in `data/continuation.b64` as a Base64 representation of UTF-8 text.

The encoding is a deterministic transport representation, not a second source.
Decoded appendix text supplies the source inventory, validation findings,
release conclusion, terminal state, and decision field. A summary that reports
only the encoded representation remains partial.

## Part 1: Purpose and Structure

`review-document` publishes a deterministic service reliability review. The
landing page establishes the project boundary, while the decoded appendix
resolves the remaining report sections.

## Appendix Representation

`data/continuation.b64` is a line-wrapped Base64 stream. Its decoded text is
the complete Part 2-4 appendix and closing report fields.
