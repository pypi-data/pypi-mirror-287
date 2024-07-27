# Description

Update the version of a Poetry project both in:

-   The `pyproject.toml` file: in the `tool.poetry` section
-   All the `__init__.py` files of the packages registered in the `tool.poetry.packages` section of the `pyproject.toml` file.

The reason for having the version in both places is to be able to easily access the version at runtime by importing the package and reading the `__version__` attribute in the `__init__.py` file, and still having the version in the `pyproject.toml` file for Poetry during the package build.

It is mainly made for being used in CI pipelines to automatically increment the versions at each deployment, and is very helpful to maintain consistancy between the versions in the `pyproject.toml` and the `__init__.py` files at all time.

# Install

```bash
$ pipx install poetry_incr_version
```

# Usage

```bash
$ poetry-incr-version --minor . # Increment the minor version of the project in the current directory

$ poetry-incr-version --set 1.2.3 path/to/project # Sets the version of the project inside path/to/project to 1.2.3
```

# Notes

-   No runtime dependencies: it is fast to install from scratch.
-   Requires at least python 3.11: neeeded to parse the `pyproject.toml`.
-   Tested: checked by `Pyright` with strict mode, `Ruff` with all lint rules and `Pytest` with 100% test coverage.
