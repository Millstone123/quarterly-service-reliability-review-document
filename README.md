# Service reliability report

`service-reliability-report` summarizes the checked-in service data and emits a
deterministic quarterly reliability report. It uses only the Python standard
library and requires no services or credentials.

## Usage

```sh
python3 -m service_reliability_report data/services.csv
```

## Verification

```sh
./verify.sh
```

The verification workflow runs the unit suite and the fixture report. The report
includes observed availability, incident count, affected requests, and the
highest-impact service row. The fixture is reviewable CSV text.
