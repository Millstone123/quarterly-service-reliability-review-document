test:
	python3 -m unittest discover -s tests -t .
	python3 -m report_pipeline data/manifest.csv
