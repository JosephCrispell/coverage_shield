[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Code Coverage](https://img.shields.io/badge/coverage-77.1%25-green)

# python_coverage_badge
A package to create and maintain a package unit test coverage badge in python code README. Importantly there are quite a few python packages that do this task or similar:
- [`genbadge`](https://smarie.github.io/python-genbadge/) - generates badges (as images) for a range of python tools including a coverage one
- [`coverage-badge`](https://pypi.org/project/coverage-badge/) - generates badge as image
- [`readme-coverage-badger`](https://pypi.org/project/readme-coverage-badger/) - adds coverage badge to README if you have already run tests

I created the `python_coverage_badge` package mainly as a learning exercise for myself but also to have a tool that runs my tests and updates a coverage badge in one go.

It works by first running the [`coverage`](https://coverage.readthedocs.io/) python package to generate a coverage report and puts the result into a structure url using the [shields.io](https://shields.io/) service. For example, the `average_coverage` and `badge_colour` variables can be fed into this url structure:
```
https://img.shields.io/badge/coverage-{average_coverage}%25-{badge_colour}
```

# Tasks

- TODO Add command line interface
- TODO Add error checking for when tests fail

# Installing `python_coverage_badge` 📦
To install this package, follow these two steps:
1. Clone the repository with (or something similar): `git clone https://github.com/JosephCrispell/python_coverage_badge.git`
2. Navigate to the repository and install with: `pip install .`

# Updating coverage badge 🔃
To update the coverage badge of your repo, run the following from within the **root** folder of your repository:
```bash
python -m python_coverage_badge
```


# Install `python_coverage_badge` 📦
Clone the repository with (or similar):
```bash
git clone https://github.com/JosephCrispell/timesheet.git
```

And install by running this in repository:
```bash
pip install -e .
```
> Note the `-e` in above means the package will automatically update as you change the codebase.

# For Developers

## Installation for development
As [above](#updating-coverage-badge-🔃) to install clone the repo but run `pip install -e .`. The `-e` flag means the package will automatically update as you change the codebase.

## Package structure
Directory tree generated using [file-tree-generator](https://marketplace.visualstudio.com/items?itemName=Shinotatwu-DS.file-tree-generator) Visual Studio Code extension:

```
📦python_coverage_badge
 ┣ 📂python_coverage_badge
 ┃ ┣ 📜__main__.py # script that is called when you call package (python -m python_coverage_badge)
 ┃ ┣ 📜unittest_coverage_functions.py # functions to calculate coverage and update badge
 ┃ ┗ 📜__init__.py
 ┣ 📂tests
 ┃ ┣ 📜test_unittest_coverage_functions.py # unit tests
 ┃ ┗ 📜__init__.py
 ┣ 📜.gitignore
 ┣ 📜.pre-commit-config.yaml # precommit workflow
 ┣ 📜LICENSE
 ┣ 📜README.md
 ┣ 📜requirements.txt
 ┗ 📜setup.py
```

## `precommit` installation ✔

Install python [`pre-commit`](https://pre-commit.com/) with:
```bash
pip install pre-commit
```

Within repository folder run:
```bash
pre-commit install
```

## Running tests 🧪
[Unit tests](https://realpython.com/python-testing/) (using the [`unittest`](https://docs.python.org/3/library/unittest.html) package) are in `tests/` can be ran with.

To run all tests together:
```bash
python -m unittest
```

## Workflow ➡
I created the following simple diagram using [mermaid](https://mermaid.js.org/) to show how the code and outputs link together.

```mermaid
  graph TD
    coverage_functions[python_coverage_badge/unittest_coverage_functions.py] .-> main[python_coverage_badge/__main__.py];
    coverage_functions .-> test_coverage[tests/test_unittest_coverage_functions.py];
    main --> readme[README.md];
    subgraph "unittests"
        test_coverage[tests/test_unittest_coverage_functions.py];
    end
    unittests .-> main
```
