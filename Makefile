PYTHON ?= python3

.PHONY: test summary

test:
	$(PYTHON) -m unittest discover -v

summary: test
	$(PYTHON) -m service_review.cli --summary
