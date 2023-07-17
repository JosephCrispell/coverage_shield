 [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
 ![Code Coverage](https://img.shields.io/badge/coverage-83.0%25-green)

# python_coverage_badge
A package to create and maintain a package unit test coverage badge in python code README

# Tasks

- TODO Add link to better coverage package
- TODO Update this README and simplify setup content below
- TODO Add workflow diagram
- TODO Add doctree


# Updating coverage badge 🦡
To update the coverage badger of this README run:
```python
python main.py
```
This script uses the [`coverage`](https://coverage.readthedocs.io/) python package to generate a coverage report and then feeds overall test coverage value into badge for this README.
> Note must be ran from repository root as shown in above codeblock

# Install `python_coverage_badge` 🦡
Clone the repository with (onote this is for https based link, change to suit your setup):
```bash
git clone https://github.com/JosephCrispell/timesheet.git
```

And install by navigating to repository and running:
```bash
pip install -e .
```
Note the `-e` in above means the package will automatically update as you change the codebase.

# `precommit` installation ✔

Install python `pre-commit` with:
```bash
pip install pre-commit
```

Within repository folder run:
```bash
pre-commit install
```

The hooks within `.pre-commit-config.yaml` will now be triggered every time you use the `git commit` command. For more information see [pre-commit.com/](https://pre-commit.com/).

# Running tests 🧪
Unit tests for package are in `tests/` can be ran all together or individually, after running:
```bash
pip install -e .
```

To run all tests together:
```bash
python -m unittest
```

To run specific tests on `timesheet.py`:
```bash
python tests/test_timesheet.py
```

For more information see:
- [`unittest`](https://docs.python.org/3/library/unittest.html) package
- [Tutorial I found helpful](https://realpython.com/python-testing/)
