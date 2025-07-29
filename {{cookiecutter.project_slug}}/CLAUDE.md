# {{ cookiecutter.project_name }} - Claude Instructions

This document contains project-specific instructions for Claude when working on this codebase.

## Project Overview

{{ cookiecutter.project_description }}

## Code Standards

This project enforces strict code quality standards:

### Code Complexity Limits
- **Max 50 lines per function** - Split larger functions
- **Cyclomatic complexity ≤ 8** - Simplify complex logic  
- **Max 5 positional parameters** - Use keyword arguments or dataclasses
- **Max 12 branches per function** - Extract to helper functions
- **Max 6 return statements** - Consolidate exit points

### Style Guidelines
- **Line length**: 100 characters max
- **Docstrings**: Google style on all public functions/classes
- **Type hints**: Required for all function signatures
- **Tests**: Must live beside code (`test_*.py` or `*_test.py`)

## Quick Commands

```bash
# Development setup
make dev

# Run all checks
make check  # Runs lint + tests

# Code quality
make lint   # ruff format --check + ruff check + ty check
make fix    # Auto-fix formatting and lint issues
make ty     # Run type checker with strict mode

# Testing
make test   # Run pytest with coverage

# Development
{% if cookiecutter.entry_point -%}
make run ARGS="--help"  # Run the CLI
{%- endif %}
{%- if cookiecutter.web_framework == "fastapi" %}
make serve  # Run FastAPI dev server on http://localhost:8000
{%- endif %}
make doc    # Build documentation
```

## Project Structure

```
src/
└── {{ cookiecutter.__project_import.replace('.', '/') }}/
    ├── __init__.py
    {%- if cookiecutter.entry_point %}
    ├── __main__.py      # CLI entry point
    ├── _cli.py          # CLI implementation
    {%- endif %}
    └── py.typed         # Type checking marker

test/
└── test_*.py            # Traditional test location
```

Tests can also live beside source files as `test_*.py` or `*_test.py`.

## Key Libraries

{%- if cookiecutter.data_library == "polars" %}
- **Data processing**: Polars (preferred over pandas)
  ```python
  import polars as pl
  df = pl.DataFrame({"col": [1, 2, 3]})
  ```
{%- elif cookiecutter.data_library == "pandas" %}
- **Data processing**: Pandas
  ```python
  import pandas as pd
  df = pd.DataFrame({"col": [1, 2, 3]})
  ```
{%- endif %}

{%- if cookiecutter.web_framework == "fastapi" %}
- **Web framework**: FastAPI (never use Flask)
  ```python
  from fastapi import FastAPI
  
  app = FastAPI()
  
  @app.get("/")
  async def root():
      return {"message": "Hello World"}
  ```
{%- endif %}

## Framework Preferences

- **Web**: Always use FastAPI, never Flask
- **Data**: Prefer Polars over Pandas for new code
- **Async**: Use native async/await, not threading

## Common Patterns

### Error Handling
```python
from typing import Result  # If using result types

def process_data(path: str) -> Result[Data, str]:
    """Process data from file.
    
    Args:
        path: Path to data file.
        
    Returns:
        Result with Data on success, error message on failure.
    """
    try:
        # Implementation
        return Ok(data)
    except Exception as e:
        return Err(f"Failed to process: {e}")
```

### Logging
```python
import logging

logger = logging.getLogger(__name__)
```

{%- if cookiecutter.entry_point %}

### CLI Arguments
Use the existing `_cli.py` structure:
```python
parser.add_argument(
    "--verbose", "-v",
    action="store_true",
    help="Enable verbose output"
)
```
{%- endif %}

## Testing Guidelines

- Aim for 100% test coverage (enforced by CI)
- Use `pytest.mark.parametrize` for multiple test cases
- Mock external dependencies
- Test both success and error paths

## CI/CD

GitHub Actions run on every push/PR:
1. **Linting**: ruff format/check + ty type checking
2. **Tests**: pytest with coverage
3. **Security**: zizmor workflow scanning
{%- if cookiecutter.documentation == "pdoc" %}
4. **Docs**: Auto-deploy to GitHub Pages
{%- endif %}

## Important Notes

1. **Never commit code that violates the quality standards** - refactor instead
2. **All public APIs need Google-style docstrings**
3. **Type hints are mandatory** - use `ty check`
4. **Tests can live beside code** - prefer colocated tests for better maintainability

## Project-Specific Instructions

<!-- Add any project-specific Claude instructions here -->

---
*This file helps Claude understand project conventions. Update it as patterns emerge.*