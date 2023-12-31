[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Code Coverage](https://img.shields.io/badge/coverage-83.4%25-54b45f)
[![Python package](https://github.com/JosephCrispell/coverage_shield/actions/workflows/python-package-build.yml/badge.svg)](https://github.com/JosephCrispell/coverage_shield/actions/workflows/python-package-build.yml)

<img src="images/logo.svg" alt="timesheet logo" align="right" width="15%">

# coverage_shield
A package to create and maintain a package unit test coverage badge in python code README. Importantly there are quite a few python packages that do this task or similar:
- [`genbadge`](https://smarie.github.io/python-genbadge/) - generates badges (as images) for a range of python tools including a coverage one
- [`coverage-badge`](https://pypi.org/project/coverage-badge/) - generates badge as image
- [`readme-coverage-badger`](https://pypi.org/project/readme-coverage-badger/) - adds coverage badge to README if you have already run tests

I created the `coverage_shield` package mainly as a learning exercise for myself but also to have a tool that runs my tests and updates a coverage badge in one go.

It works by first running the [`coverage`](https://coverage.readthedocs.io/) python package to generate a coverage report and puts the result into a structure url using the [shields.io](https://shields.io/) service. For example, the `average_coverage` and `badge_colour` variables can be fed into this url structure:
```
https://img.shields.io/badge/coverage-{average_coverage}%25-{badge_colour}
```

# Tasks

- TODO create a release
- TODO look into getting published on pip
- TODO improve coverage of tests for git functions if possible

# Installing `coverage_shield` 📦
To install this package, follow these two steps:
1. Clone the repository with (or something similar): `git clone https://github.com/JosephCrispell/coverage_shield.git`
2. Navigate to the repository and install with: `pip install .`

# Updating coverage badge 🔃
To update the coverage badge of your repo, run the following from within the **root** folder of your repository:
```bash
python -m coverage_shield
```

There are a few command line arguments you can use, take a look with `python -m coverage_shield --help`:
```
usage: coverage_shield [-h] [-d [directory]] [-r [readme_path]] [-t [tester]] [-g]

Welcome to coverage_shield! A tool to create and maintain a python package unit test coverage badge in README.md

options:
  -h, --help            show this help message and exit
  -d [directory], --directory [directory]
                        Provide path to directory to run coverage_shield in. (default: .)
  -r [readme_path], --readme [readme_path]
                        Provide path to README.md relative to directory provided. (default: README.md)
  -t [tester], --tester [tester]
                        Provide name of unit test python package you want to use. Accepts either "unittest" or "pytest" (default: unittest)
  -g, --git_push        Stage, commit, and push the updated README file (-r/--readme) using git. (default: False)
```

# Ignoring patterns

If you'd like to ignore the unit test coverage for particular files in your coverage report you can created a `.covignore` file in your repository directory. For example, here's the content of the `.covignore` file for this project:

```
setup.py
__init__.py
```

The `.covignore` works in a similar way to a `.gitignore` file and any pattern found in it is passed to the [`str.contains()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.contains.html) function and used to filter the unit test coverage report before calculate the average coverage for the project. So the above means that any `setup.py` or `__init__.py` files are ignored.

# For Developers

## Installation for development
As [above](#updating-coverage-badge-🔃) to install clone the repo but run `pip install -e .`. The `-e` flag means the package will automatically update as you change the codebase.

## Package structure
Directory tree generated using [file-tree-generator](https://marketplace.visualstudio.com/items?itemName=Shinotatwu-DS.file-tree-generator) Visual Studio Code extension:

```
📦coverage_shield
 ┣ 📂coverage_shield
 ┃ ┣ 📜__main__.py # script that is called when you call package (python -m coverage_shield)
 ┃ ┣ 📜command_line_interface_functions.py # functions for the command line interface
 ┃ ┣ 📜git_functions.py # functions to staging, committing, and pushing updated README to remote
 ┃ ┣ 📜unittest_coverage_functions.py # functions to calculate coverage and update badge
 ┃ ┗ 📜__init__.py # package structure/info
 ┣ 📂images
 ┃ ┗ 📜logo.svg
 ┣ 📂tests
 ┃ ┣ 📜test_command_line_interface_functions.py # unit tests for cli
 ┃ ┣ 📜test_git_functions.py # unit tests for git functions
 ┃ ┣ 📜test_main.py # unit tests for main script
 ┃ ┣ 📜test_unittest_coverage_functions.py # unit tests for functions to create/update coverage badge
 ┃ ┗ 📜__init__.py # package structure/info
 ┣ 📜.covignore # patterns/files to ignore when calculating coverage
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

Within repository folder run to install hooks:
```bash
pre-commit install
```

## Running tests 🧪
[Unit tests](https://realpython.com/python-testing/) (using the [`unittest`](https://docs.python.org/3/library/unittest.html) package) are in `tests/` can be ran all together with:
```bash
python -m unittest
```

## Workflow ➡
I created the following simple diagram using [mermaid](https://mermaid.js.org/) to show how the code and outputs link together.

```mermaid
  graph TD
    coverage_functions[coverage_shield/unittest_coverage_functions.py] .-> main[coverage_shield/__main__.py];
    coverage_functions .-> test_coverage[tests/test_unittest_coverage_functions.py];
    main --> readme[README.md];
    main .-> test_main[tests/test_main.py];
    cli_functions[coverage_shield/command_line_interface_functions.py] .-> main;
    cli_functions .-> test_cli[tests/test_command_line_interface_functions.py];
    git_functions[coverage_shield/git_functions.py] .-> main;
    git_functions .-> test_git[tests/test_git_functions.py];
    subgraph "unittests"
        test_coverage;
        test_cli;
        test_git;
        test_main;
    end
    unittests .-> coverage_functions
```
