#!/bin/sh
set -eu
python3 -m unittest discover -s tests -t .
python3 -m doctest README.md
python3 -m command_gated_summary --continue data/manifest.csv
python3 -c 'from command_gated_summary.compatibility import compatibility_version; print("compatibility=" + compatibility_version())'
