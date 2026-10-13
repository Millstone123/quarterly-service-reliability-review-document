# Release Review Document: Part 1 of 3

This checked-in text is the first part of the release review. The source
inventory, validation findings, and release conclusion are distributed across
repository text inputs and are not included in this landing file.

Complete the review through the ordinary report command:

```sh
python3 -m command_gated_summary --continue data/manifest.csv
```

The command resolves the distributed review inputs, prints Parts 2 and 3, and
runs the checked-in compatibility check. `./verify.sh` runs the local tests and
the same continuation command.
