test:
	python3 -m unittest discover -s tests -t .
document:
	python3 -m doctest README.md
report:
	python3 -m command_gated_summary --continue data/manifest.csv
verify:
	./verify.sh
