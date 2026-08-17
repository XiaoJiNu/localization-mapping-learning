PYTHON ?= python3

.PHONY: install test smoke experiment lint format markdown check

install:
	$(PYTHON) -m pip install -e ".[dev]"

test:
	PYTHONPATH=src $(PYTHON) -m pytest

smoke:
	PYTHONPATH=src $(PYTHON) -m unittest discover -s tests -v

experiment:
	$(PYTHON) experiments/exp_001_transform_chain/run.py

lint:
	$(PYTHON) -m ruff check src tests experiments

format:
	$(PYTHON) -m ruff format src tests experiments

markdown:
	$(PYTHON) src/localization_learning/markdown_check.py .

check: test lint markdown experiment
