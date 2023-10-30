"""The `python -m {{ cookiecutter.project_slug }}` entrypoint."""

if __name__ == "__main__":  # pragma: no cover
    from {{ cookiecutter.__project_import }}._cli import main

    main()
