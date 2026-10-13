.PHONY: all report test

all: report

report:
	mkdir -p build
	python3 -m data.review_continuation > build/review.md

test:
	python3 -m unittest discover -s tests -t .
