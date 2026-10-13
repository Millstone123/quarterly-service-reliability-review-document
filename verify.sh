#!/bin/sh
set -eu
python3 -m unittest discover -s tests -t .
python3 -m terminal_report data/manifest.csv --continue
