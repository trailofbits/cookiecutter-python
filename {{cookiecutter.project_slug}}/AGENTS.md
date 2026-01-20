# AGENTS.md

## Project Overview

{{ cookiecutter.project_description }}

{%- if cookiecutter.repo_type == 'CLI' %}
This is a command-line application with entry point `{{ cookiecutter.entry_point }}`.
{%- else %}
This is a Python library package.
{%- endif %}

## Stack

- Package manager: uv
- Build backend: uv_build
- Linting/formatting: ruff
- Type checking: ty
- Testing: pytest
- CI: GitHub Actions (lint, test, release{%- if cookiecutter.documentation != 'none' %}, docs{%- endif %})

## Commands

Use Makefile targets, not tool commands directly:

- `make format` - Fix formatting issues
- `make lint` - Run all static checks (ruff, ty)
- `make test` - Run tests with coverage
- `make doc` - Generate documentation
- `make build` - Build the package
{%- if cookiecutter.entry_point %}
- `make run` - Run the CLI (use `ARGS="..."` for arguments)
{%- endif %}

## Verification

Run `make lint && make test` before committing.

## Commit Messages

- Summary line: max 50 chars (hard limit 72)
- Body lines: max 72 chars
- Use Markdown formatting in description
- Reference issues where relevant (e.g., `See #123`)

## Project Layout

- `src/{{ cookiecutter.__project_import.replace('.', '/') }}/` - Source code
- `test/` - Test files
