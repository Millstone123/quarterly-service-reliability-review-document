# Quarterly Service Reliability Review Document

This repository packages one generated review document. The readable report
body is not duplicated in Markdown or repository metadata.

`review-package.txt` is an encoded compressed package containing the report
body and verification metadata. The package is checked in so the report can be
reproduced offline. Recovering the report body means decoding that package.

The source tree contains the reader, package verification, and tests.
