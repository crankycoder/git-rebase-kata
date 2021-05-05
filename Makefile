.PHONY: create_venv

all:
	python setup.py build

pin_versions:
	pip-compile --generate-hashes requirements.in

create_venv:
	python3 -m venv .venv

run:
	./run.sh
