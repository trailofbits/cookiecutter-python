# cookiecutter-python

This repository contains a
[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template
for a Python package.

It's designed primarily for Trail of Bits' own use, but should be usable
by anyone.

Both command-line and library packages can be generated.

## Usage

Install the `cookiecutter` CLI:

```
python -m pip install cookiecutter
```

Use `cookiecutter` to generate a project using this template:

```bash
# creates the project directory in $PWD
cookiecutter gh:trailofbits/cookiecutter-python
```

Alternatively, tell `cookiecutter` where to put the new project directory:

```bash
# creates ~/tmp/$project
cookiecutter -o ~/tmp gh:trailofbits/cookiecutter-python
```

`cookiecutter` will prompt you for the project's name and all other relevant
metadata.
