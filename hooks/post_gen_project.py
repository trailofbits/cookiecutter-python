import os
import sys

REMOVE_PATHS = [
    # We delete _cli.py and __main__.py if we're not generating a CLI.
    "{% if cookiecutter.entry_point == '' %} {{ cookiecutter.module_slug }}/_cli.py {% endif %}",
    "{% if cookiecutter.entry_point == '' %} {{ cookiecutter.module_slug }}/__main__.py {% endif %}",
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)
