SHELL := /bin/bash

PY_IMPORT = {{ cookiecutter.__project_import }}

ALL_PY_SRCS := $(shell find src -name '*.py') \
	$(shell find test -name '*.py')

# Optionally overriden by the user, if they're using a virtual environment manager.
VENV ?= env

# On Windows, venv scripts/shims are under `Scripts` instead of `bin`.
VENV_BIN := $(VENV)/bin
ifeq ($(OS),Windows_NT)
	VENV_BIN := $(VENV)/Scripts
endif

# Optionally overridden by the user in the `release` target.
BUMP_ARGS :=

# Optionally overridden by the user in the `test` target.
TESTS :=

# Optionally overridden by the user/CI, to limit the installation to a specific
# subset of development dependencies.
INSTALL_EXTRA := dev

# If the user selects a specific test pattern to run, set `pytest` to fail fast
# and only run tests that match the pattern.
# Otherwise, run all tests and enable coverage assertions, since we expect
# complete test coverage.
ifneq ($(TESTS),)
	TEST_ARGS := -x -k $(TESTS)
	COV_ARGS :=
else
	TEST_ARGS :=
	COV_ARGS := --fail-under 100
endif

.PHONY: all
all:
	@echo "Run my targets individually!"

.PHONY: dev
dev: $(VENV)/pyvenv.cfg

{%- if cookiecutter.entry_point %}
.PHONY: run
run: $(VENV)/pyvenv.cfg
	@. $(VENV_BIN)/activate && {{ cookiecutter.entry_point }} $(ARGS)
{%- endif %}

$(VENV)/pyvenv.cfg: pyproject.toml
	# Create our Python 3 virtual environment
	python3 -m venv env
	# NOTE(ekilmer): interrogate v1.5.0 needs setuptools when using Python 3.12+.
	# This should be fixed when the next release is made
	$(VENV_BIN)/python -m pip install --upgrade pip setuptools
	$(VENV_BIN)/python -m pip install -e .[$(INSTALL_EXTRA)]

.PHONY: lint
lint: $(VENV)/pyvenv.cfg
	. $(VENV_BIN)/activate && \
		ruff format --check $(ALL_PY_SRCS) && \
		ruff $(ALL_PY_SRCS) && \
		mypy

	{%- if cookiecutter.docstring_coverage %}
	. $(VENV_BIN)/activate && \
		interrogate -c pyproject.toml .
	{%- endif %}

.PHONY: reformat
reformat:
	. $(VENV_BIN)/activate && \
		ruff --fix $(ALL_PY_SRCS) && \
		ruff format $(ALL_PY_SRCS)

.PHONY: test tests
test tests: $(VENV)/pyvenv.cfg
	. $(VENV_BIN)/activate && \
		pytest --cov=$(PY_IMPORT) $(T) $(TEST_ARGS) && \
		python -m coverage report -m $(COV_ARGS)

.PHONY: doc
{%- if cookiecutter.documentation == 'pdoc' %}
doc: $(VENV)/pyvenv.cfg
	. $(VENV_BIN)/activate && \
		pdoc -o html $(PY_IMPORT)
{%- elif cookiecutter.documentation == 'none' %}
doc:
	@echo "No documentation set up"
{%- endif %}

.PHONY: package
package: $(VENV)/pyvenv.cfg
	. $(VENV_BIN)/activate && \
		python3 -m build

.PHONY: edit
edit:
	$(EDITOR) $(ALL_PY_SRCS)
