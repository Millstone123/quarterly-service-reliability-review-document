#!/bin/sh
set -eu
python3 -m unittest discover -s tests -t .
python3 -m service_reliability_report data/services.csv
