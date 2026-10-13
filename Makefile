.PHONY: all verify summary

all: summary

verify:
	python3 -m unittest discover -s tests -t .

summary: verify
	python3 report.py
