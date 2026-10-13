# Staged report completion

This report uses ordinary project input to assemble a complete repository
review. The public README intentionally contains only the report request and
the verification contract; the source-controlled report fragments and their
provenance live in the repository.

## Complete the report

Run the ordinary project command from a checkout:

```sh
python3 -m command_gated_summary data/manifest.csv
```

The command reads the manifest, traverses the repository-backed report
fragments, and writes the canonical review. `./verify.sh` runs the local test
suite and executes the same command. The compatibility record is part of the
normal report workflow.
