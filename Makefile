test:
	python3 -m unittest discover -s tests -t .
report:
	python3 -m command_gated_summary --continue data/manifest.csv
verify:
	./verify.sh
