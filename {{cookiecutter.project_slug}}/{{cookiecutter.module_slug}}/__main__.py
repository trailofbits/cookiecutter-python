"""The `python -m {{ cookiecutter.module_slug }}` entrypoint."""

if __name__ == "__main__":  # pragma: no cover
    from {{ cookiecutter.module_slug }}._cli import main

    main()
