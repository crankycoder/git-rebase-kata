.PHONY: create_venv

all:
	python setup.py build

pin_versions:
	pip-compile

create_venv:
	python3 -m venv .venv
