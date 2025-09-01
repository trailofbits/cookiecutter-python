SHELL := /bin/bash

PY_IMPORT = {{ cookiecutter.__project_import }}

# Optionally overridden by the user in the `test` target.
TESTS :=

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

{%- if cookiecutter.entry_point %}
.PHONY: run
run:
	uv run {{ cookiecutter.entry_point }} $(ARGS)
{%- endif %}

.PHONY: lint
lint:
	uv run ruff format --check && \
		uv run ruff check && \
		uv run mypy

	{%- if cookiecutter.docstring_coverage %}
		uv run interrogate -c pyproject.toml .
	{%- endif %}

.PHONY: format
format:
	uv run ruff format && \
		uv run ruff check --fix

.PHONY: test
test:
	uv run pytest --cov=$(PY_IMPORT) $(T) $(TEST_ARGS)
	uv run coverage report -m $(COV_ARGS)

.PHONY: doc
{%- if cookiecutter.documentation == 'pdoc' %}
doc:
	uv run pdoc -o html $(PY_IMPORT)
{%- elif cookiecutter.documentation == 'none' %}
doc:
	@echo "No documentation set up"
{%- endif %}

.PHONY: build
build:
	uv build
