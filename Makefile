all: report

report:
	mkdir -p build
	python3 reader.py > build/review.md

summary:
	python3 reader.py --continue 1
	python3 reader.py --continue 2
	python3 reader.py --continue 3

test:
	python3 -m unittest discover -s tests -t .
	python3 reader.py --verify
