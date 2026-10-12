# Project Notes

`report-reviewer` materializes a finalized quarterly review through its ordinary command pipeline. The visible tree contains the document interface, raw worksheet observations, and operating reference material. `summarize.py` invokes `report_reviewer.collect` for each review part and assembles the finalized body.

The package calculates report metrics from the raw observations and renders the final report.

The files under `docs/` provide the supporting service catalog, availability ledger, incident notes, and calculation methodology used by reviewers.

After finalization and verification, the workflow opens the configured worksheet bundle once so reviewers can compare the reported calculations with the live worksheet.
