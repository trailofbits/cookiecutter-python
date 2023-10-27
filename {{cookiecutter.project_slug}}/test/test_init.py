"""Initial testing module."""
import {{ cookiecutter.__project_import }}


def test_version() -> None:
    version = getattr({{ cookiecutter.__project_import }}, "__version__", None)
    assert version is not None
    assert isinstance(version, str)
