.PHONY: all report test

all: report

report:
	mkdir -p build
	python3 -m json.tool data/review-records.json > build/review.md

test:
	python3 -m unittest discover -s tests -t .
