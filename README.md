# Service Reliability Review

`review-document` is a small, standard-library Python project that turns tracked service measurements and compatibility profiles into a deterministic reliability review. The package has no runtime dependencies and exposes a normal command-line report entrypoint.

## Project setup

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
python -m unittest discover -v
service-review --summary
```

## Report

The generated summary contains release measurements, compatibility resolution, runtime identity, and a closing recommendation. The checked-in tests cover the measurement parser, profile resolver, report rendering, and command-line output. The `service-review --summary` command is the canonical way to obtain the complete report from the checked-in inputs.

## Layout

- `service_review/` contains the package and CLI.
- `data/measurements.csv` contains the tracked request measurements.
- `compatibility_profiles.json` contains the supported runtime profiles.
- `tests/` contains the ordinary local test suite.
