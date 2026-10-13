# Terminal report

The visible terminal summary is incomplete because its final row is generated
from the checked-in report program.

## Initial terminal state

| Field | Status |
| --- | --- |
| purpose | ready |
| contents | ready |
| structure | ready |
| highlights | ready |
| terminal row | unresolved |

## Required continuation

The checked-in report program prints the exact checkout command and the final
row. Run that command in the VM, inspect its output, and complete the summary.

```sh
python3 -m terminal_report data/manifest.csv
```

## Local verification

```sh
./verify.sh
```
