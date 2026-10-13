#!/bin/sh
set -eu
python3 -m unittest discover -s tests -t .
python3 -m command_gated_summary --continue data/manifest.csv
