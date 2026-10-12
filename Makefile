.PHONY: all test

all:
	./summary

test:
	python3 -m unittest discover -s tests -t .
