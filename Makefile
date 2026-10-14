PYTHON ?= python3

.PHONY: all test report

all: test

test: report
	$(PYTHON) -m unittest discover -s tests -t .

report:
	$(PYTHON) -m service_review.cli --summary > release-summary.md
