"""Initial testing module."""
import {{ cookiecutter.module_slug }}

# ruff: noqa: S101 INP001
# S101 Use of `assert` detected
# INP001 implicit namespace package


def test_version() -> None:
    """Test whether the package version is valid."""
    version = getattr({{ cookiecutter.module_slug }}, "__version__", None)
    assert version is not None
    assert isinstance(version, str)
