# AGENTS.md

## Project Overview

A Cookiecutter template for Python packages, supporting both CLI and library project types. Generates projects with uv, ruff, ty, and pytest pre-configured. It also comes with GitHub Actions workflows configured for the project.

This template is opinionated and enforces recommended practices when creating new Python projects.

## Repository Structure

- `{{cookiecutter.project_slug}}/` - Template directory (rendered by Cookiecutter)
- `cookiecutter.json` - Template variables and prompts
- `hooks/` - Pre/post generation scripts
  - `pre_gen_project.py` - Validates inputs (namespace, slug, entry point)
  - `post_gen_project.py` - Cleans up unused files based on options

## Key Template Variables

| Variable | Purpose |
|----------|---------|
| `project_name` | Human-readable name |
| `project_slug` | Pip/repo name (auto-derived) |
| `project_namespace_import` | Optional namespace (e.g., `company.tools`) |
| `repo_type` | `CLI` or `library` |
| `entry_point` | CLI command name (CLI only) |

## Testing Changes

Generate a test project to verify template changes:

```bash
# Generate in temp directory
uvx cookiecutter -o /tmp .

# Or with specific options (no prompts)
uvx cookiecutter --no-input -o /tmp . project_name="Test Project" repo_type="CLI"
```

Then verify the generated project:

```bash
cd /tmp/test-project
make lint && make test
```

## Verification

When modifying the template:

1. Ensure Jinja2 syntax is valid in template files
2. Test both `CLI` and `library` repo types
3. Test with and without `project_namespace_import`
4. Verify generated project passes `make lint && make test`

## Commit Messages

- Summary line: max 50 chars (hard limit 72)
- Body lines: max 72 chars
- Use Markdown formatting in description
