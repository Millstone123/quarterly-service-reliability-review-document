# Report pipeline

`report-pipeline` is a dependency-free Python package that reads the checked-in
data manifest and generates a deterministic report. The generated report is the
package output; the GitHub landing page is only an index.

## Workflow

```sh
python3 -m report_pipeline data/manifest.csv
```

## Verification

```sh
./verify.sh
```

The report contains the source rows, totals, and a release-impact classification.
All source data is checked-in text and can be reviewed before the report runs.
