.PHONY: all report test

all: report

report:
	mkdir -p build
	python3 reader.py > build/review.md

test:
	python3 -m unittest discover -s tests -t .
	python3 reader.py --verify
