import os

REMOVE_PATHS = [
    # We delete _cli.py and __main__.py if we're not generating a CLI.
    "{% if cookiecutter.entry_point == '' %} {{ cookiecutter.__project_src_path }}/_cli.py {% endif %}",
    "{% if cookiecutter.entry_point == '' %} {{ cookiecutter.__project_src_path }}/__main__.py {% endif %}",
    # We delete the docs GH workflow if the project has no documentation
    "{% if cookiecutter.documentation == 'none' %} .github/workflows/docs.yml {% endif %}",
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)

# Potentially new directory for namespace project
namespace_project_dir = os.path.join(
    os.getcwd(), "{{ cookiecutter.__project_src_path }}"
)
if not os.path.exists(namespace_project_dir):
    module_dir = os.path.join(os.getcwd(), "src", "{{ cookiecutter.__module_import }}")
    os.makedirs(namespace_project_dir)
    os.rename(module_dir, os.path.join(namespace_project_dir))
