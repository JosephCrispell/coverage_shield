# Load packages
import argparse  # parsing command line arguments
from pathlib import Path  # handling file paths
from datetime import datetime  # working with dates and times
import sys  # accessing command line arguments
import os  # Change directory

# Local imports
from python_coverage_badge import unittest_coverage_functions
from python_coverage_badge import git_functions

# TODO add git argument


def build_command_line_interface() -> argparse.ArgumentParser:
    """Builds command line interface for python_coverage_badge package

    Adds the following arguments:
    - Target directory: -d/--directory
    - Target README: -r/--readme
    - Push changes: -g/--git_push

    Returns:
        argparse.ArgumentParser: argument parser
    """

    # Write welcome message
    welcome_message = "Welcome to python_coverage_badge! A tool to create and maintain a python package unit test coverage badge in README.md"

    # Initialize parser
    parser = argparse.ArgumentParser(
        prog="python_coverage_badge",
        description=welcome_message,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,  # Shows default values for parameters
    )

    # Add arguments
    parser.add_argument(
        "-d",
        "--directory",
        nargs="?",  # Accept 0 or 1 arguments
        default=".",  # Default value
        metavar="directory",
        type=str,
        help="Provide path to directory to run python_coverage_badge in.",
    )
    parser.add_argument(
        "-r",
        "--readme",
        nargs="?",  # Accept 0 or 1 arguments
        default="README.md",  # Default value
        metavar="readme_path",
        type=str,
        help="Provide path to README.md relative to directory provided.",
    )
    parser.add_argument(
        "-g",
        "--git_push",
        action="store_false",
        help="Stage, commit, and push the updated README file (-r/--readme) using git.",
    )

    return parser


def parse_command_line_arguments(
    parser: argparse.ArgumentParser,
    arguments: list[str] = sys.argv[1:],
    testing: bool = False,
):
    """Parse command line arguments based on parser provided

    Args:
        parser (argparse.ArgumentParser): command line argument parser
        arguments (list[str]): list of command line arguments passed to parser.parse_args(), which isn't
            required normally but this means we can unittest
            (see: https://stackoverflow.com/questions/18160078/how-do-you-write-tests-for-the-argparse-portion-of-a-python-module).
            Defaults to sys.argv[:1] (arguments minus script name).
        testing (bool): check if running unit tests as don't want to run coverage package if we are. Defaults to False.
    """

    # Get arguments
    args = parser.parse_args(arguments)

    # Check if running unittests
    if not testing:

        # Set target directory
        os.chdir(args.directory)

        # Run coverage package (which runs unittests and generates report
        coverage_dataframe = unittest_coverage_functions.run_code_coverage()

        # Build the badge url
        coverage_badge_url = unittest_coverage_functions.make_coverage_badge_url(
            coverage_dataframe
        )

        # Update badge in README
        unittest_coverage_functions.replace_regex_in_file(
            file_path=Path(args.directory, args.readme),
            pattern_regex=r"\!\[Code Coverage\]\(.+\)",
            replacement=f"![Code Coverage]({coverage_badge_url})",
        )

        # Check if pushing changes
        if args.git_push:

            # Stage, commit, and push updated README
            git_functions.push_updated_readme(
                readme_path=Path(args.directory, args.readme)
            )

    else:
        return args
