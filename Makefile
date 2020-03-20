MODULE := dslr
DATAPATH := ./resources/dataset_train.csv
WATCH_CMD :=python dslr/histogram/histogram.py ./resources/dataset_train.csv

BLUE=\033[0;34m
NC=\033[0m # No Color

.PHONY: run test clean pytest

run:
	@python -m dslr $(DATAPATH)

watch:
	@watchmedo shell-command \
		--pattern="*.py" \
		--recursive \
		--command='echo "${watch_src_path}" && $(WATCH_CMD) && pytest' \
		.

test:
	@coverage run --rcfile=.config/setup.cfg -m pytest
	@echo "\n$(BLUE)Coverage$(NC)\n"
	@coverage report -m
	@echo "\n$(BLUE)Security check$(NC)\n"
	@bandit -r --ini .config/setup.cfg

clean:
	@rm -rf .pytest_cache .coverage .pytest_cache coverage.xml
