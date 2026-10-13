# Service Reliability Review

This repository contains a dependency-free Python workflow for assembling a
quarterly service reliability review from checked-in source records. The source
records are under `data/inputs/`; generated review output is intentionally not
committed.

## Project layout

- `command_gated_summary/` - report model, renderer, and compatibility resolver
- `data/` - source records and the report manifest
- `tests/` - ordinary unit tests for the workflow
- `verify.sh` - standard validation entry point

## Development

Run the standard validation entry point:

```text
./verify.sh
```

It runs the unit tests, renders the sample report from `data/manifest.csv`, and
prints the compatibility metadata for the installed workflow. The rendered
stdout is the generated review artifact; the checked-in source records are the
inputs to that workflow.

The report command is also available directly:

```text
python3 -m command_gated_summary --continue data/manifest.csv
```
