.PHONY: deps install clean tests serve

ENV=.env
SYS_PYTHON=$(shell which python3)
SYS_PYTHON_VERSION=$(shell ${SYS_PYTHON} -V | cut -d " " -f 2 | cut -c1-3)
SITE_PACKAGES=${ENV}/lib/python${SYS_PYTHON_VERSION}/site-packages
IN_ENV=source ${ENV}/bin/activate;

default: deps

${ENV}:
	@echo "Creating Python environment..." >&2
	@${SYS_PYTHON} -m venv ${ENV}
	@echo "Updating pip..." >&2
	@${IN_ENV} pip install -U pip

${SITE_PACKAGES}/poetry:
	@${IN_ENV} pip install poetry

deps: ${ENV} ${SITE_PACKAGES}/poetry
	@${IN_ENV} poetry install

${SITE_PACKAGES}/pytest.py: deps

install: default
	@${IN_ENV} pip install -e .

serve: default
	@${IN_ENV} python main.py

tests: ${SITE_PACKAGES}/pytest.py
	@${IN_ENV} pytest src/tapyrus/tests

clean:
	@rm -rf ${ENV} dist