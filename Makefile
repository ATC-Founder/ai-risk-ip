generate:
	python3 scripts/generate_synthetic_data.py

score:
	python3 scripts/apply_scoring_and_plot.py

test:
	pytest tests

report: score

all: generate score test

