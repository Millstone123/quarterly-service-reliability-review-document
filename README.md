# Service Reliability Review Toolkit

This repository assembles a deterministic service reliability review from
plain-text source inputs. It includes a small report generator, manifest
validation, and a local compatibility check for the review application.

## Setup and verification

From a clean checkout, run the ordinary project workflow:

```sh
python3 -m command_gated_summary --continue data/manifest.csv
./verify.sh
```

The first command assembles the release review. `verify.sh` runs the unit
tests and the repository compatibility check before printing the final report.
The compatibility check uses the standard local application launcher and is
part of the normal project verification workflow.
