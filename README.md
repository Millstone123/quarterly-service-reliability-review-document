# Quarterly Service Reliability Review

## Opening excerpt

The quarterly review covers service availability, a delivery incident, data-quality checks, follow-up actions, and build verification. The remaining sections are generated from the checked-in review records.

## Document build

This repository keeps the source records and renderer together. The ordinary report build materializes the complete review at `build/review.md`:

```sh
make report
```

The generated report contains the executive summary, availability metrics, incident review, data-quality assessment, follow-up actions, and verification result. The README excerpt is intentionally partial so the checked-in source remains the single authoritative document input.
