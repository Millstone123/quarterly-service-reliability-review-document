# Evidence summary runner

This repository is a dependency-free Python report program. Its checked-in
manifest records the repository's review artifacts. The program computes a
complete summary from those artifacts.

## Generate the required summary

```sh
python3 -m evidence_summary data/manifest.csv
```

## Verify the summary

```sh
./verify.sh
```

The repository's requested summary sections are synthesized by the program and
tests; running the program is the reviewable source of the complete output.
