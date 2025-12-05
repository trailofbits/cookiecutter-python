SHELL := /bin/bash

PY_IMPORT = {{ cookiecutter.__project_import }}

ALL_PY_SRCS := $(shell find src -name '*.py') \
	$(shell find test -name '*.py')

# Optionally overriden by the user, if they're using a virtual environment manager.
# Warning: changing this name to something else than '.venv' will make working with
# uv harder.
VENV ?= .venv

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
	uv run pre-commit install

{%- if cookiecutter.entry_point %}
.PHONY: run
run: $(VENV)/pyvenv.cfg
	uv run {{ cookiecutter.entry_point }} $(ARGS)
{%- endif %}

$(VENV)/pyvenv.cfg: pyproject.toml
	uv venv $(VENV)
	uv pip install -e '.[$(INSTALL_EXTRA)]'

.PHONY: lint
lint: $(VENV)/pyvenv.cfg
	uv run ruff format --check && \
		uv run ruff check && \
		uv run pyright{% if cookiecutter.docstring_coverage %} && \
		uv run interrogate -c pyproject.toml .{% endif %}

.PHONY: check
check: lint test

.PHONY: typecheck
typecheck: $(VENV)/pyvenv.cfg
	uv run pyright

.PHONY: fix
fix:
	uv run ruff format && \
		uv run ruff check --fix

# Alias for backwards compatibility
.PHONY: reformat
reformat: fix

.PHONY: test tests
test tests: $(VENV)/pyvenv.cfg
	uv run pytest --cov=$(PY_IMPORT) $(T) $(TEST_ARGS)
	uv run coverage report -m $(COV_ARGS)

.PHONY: doc
{%- if cookiecutter.documentation == 'pdoc' %}
doc: $(VENV)/pyvenv.cfg
	uv run pdoc -o html $(PY_IMPORT)
{%- elif cookiecutter.documentation == 'none' %}
doc:
	@echo "No documentation set up"
{%- endif %}

.PHONY: package
package: $(VENV)/pyvenv.cfg
	uv build

.PHONY: edit
edit:
	$(EDITOR) $(ALL_PY_SRCS)
