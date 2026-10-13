# Continuation report

`continuation-report` is a dependency-free Python program for reviewing the
checked-in manifest. The public report is intentionally incomplete until its
continuation command is executed.

## Initial review

```sh
python3 -m continuation_report data/manifest.csv
```

## Resolve the remaining summary

```sh
./verify.sh
```

The initial review marks `decision-blocked-unresolved` and the continuation
command resolves the complete summary from the same checked-in records.
