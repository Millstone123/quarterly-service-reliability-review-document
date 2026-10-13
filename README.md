# Review Document

`review-document` is a small, text-only Python CLI for turning tracked service measurements into a compact reliability review.

The repository contains the measurement fixture, a compatibility profile catalog, and a report renderer. The checked-in tests cover the renderer and the profile resolution logic.

## Usage

```sh
python3 report.py --help
python3 report.py
```

The CLI prints a Markdown review with release measurements, compatibility resolution, and a closing recommendation.

## Project layout

- `report.py` — command-line renderer
- `resolver.py` — profile resolver
- `data/measurements.csv` — tracked measurements
- `compatibility_profiles.json` — static profile catalog
- `summary_contract.json` — report field contract
- `tests/` — local tests
