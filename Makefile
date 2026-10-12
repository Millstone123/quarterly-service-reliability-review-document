.PHONY: all summary selfcheck test

all: summary

summary:
	python3 summarize.py

selfcheck:
	python3 -m report_reviewer selfcheck

test:
	python3 -m unittest discover -s tests -t . -v
