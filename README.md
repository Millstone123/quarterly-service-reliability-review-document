# Quarterly Review Reader

`quarterly-review-reader` is a dependency-free Python CLI for reading the quarterly service reliability review record.

The GitHub page is only an index. The requested summary is the complete output of the CLI's `summary` command, which materializes the Markdown review from `data/review-records.json`.

## Run the summary

```sh
git clone https://github.com/Millstone123/quarterly-service-reliability-review-document.git
cd quarterly-service-reliability-review-document
python3 renderer.py summary
```

The command is read-only and prints the executive summary, availability, incident review, data quality, follow-up actions, and build verification. Use that output as the summary source.

## Installable CLI

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .
review-reader summary
```
