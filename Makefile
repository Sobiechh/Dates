# Makefile
include .env
.PHONY: format

PYTHON_FILES := $(shell git diff --name-only --relative | grep '\.py$$' && git diff --name-only --relative | grep '\.py$$' && git ls-files --others --exclude-standard | grep '\.py$$')

format:
	autoflake --in-place --remove-unused-variables --remove-all-unused-imports $(PYTHON_FILES)
	isort --profile "black" $(PYTHON_FILES)
	black --config pyproject.toml $(PYTHON_FILES)
