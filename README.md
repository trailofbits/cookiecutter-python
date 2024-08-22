# cookiecutter-python

This repository contains a
[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template
for a Python package.

It's designed primarily for Trail of Bits' own use, but should be usable
by anyone.

Both command-line and library packages can be generated.

## Usage

- Install [`uv`](https://docs.astral.sh/uv/)

```bash
# On any platform with cURL and sh
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# With Brew
brew install uv
```

Please refer to [`uv` documentation](https://docs.astral.sh/uv/getting-started/installation/) for more installation options.

- Use `cookiecutter` to generate a project using this template:

```bash
# creates the project directory in $PWD
uvx cookiecutter gh:trailofbits/cookiecutter-python
```

Alternatively, tell `cookiecutter` where to put the new project directory:

```bash
# creates ~/tmp/$project
uvx cookiecutter -o ~/tmp gh:trailofbits/cookiecutter-python
```

`cookiecutter` will prompt you for the project's name and all other relevant
metadata.

## Note

The project will be generated using `uv`, a near drop-in replacement for 
`pip` which is still in active development.

Packages are installed using `uv pip install <package_name>` (after 
activating the virtual environment).