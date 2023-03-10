import {{ cookiecutter.module_slug }}

def test_version():
    version = getattr({{ cookiecutter.module_slug }}, "__version__", None)
    assert version is not None
    assert isinstance(version, str)
