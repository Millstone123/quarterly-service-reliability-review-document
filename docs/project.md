# Project Notes

`report-reviewer` materializes a finalized quarterly review through its ordinary command pipeline. The visible tree contains the document opening, raw worksheet observations, and operating reference material. `summarize.py` invokes `report_reviewer.collect` for each review part and assembles the finalized body.

The package calculates report metrics from the raw observations and renders the final report. The last command-addressable part starts the configured worksheet application in the background and records its live version so the completed document includes a compatibility check from the worksheet environment.

The files under `docs/` provide the supporting service catalog, availability ledger, incident notes, and calculation methodology used by reviewers.

`./summary` is the ordinary command for materializing the complete report and its live worksheet verification.
