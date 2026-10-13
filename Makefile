.PHONY: all report test

all: report

report:
	mkdir -p build
	python3 review_reader.py > build/review.md

test:
	python3 -m unittest discover -s tests -t .
	python3 review_reader.py --verify
