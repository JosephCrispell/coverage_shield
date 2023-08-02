# Load packages
import argparse  # parsing command line arguments
from pathlib import Path  # handling file paths
from datetime import datetime  # working with dates and times
import sys  # accessing command line arguments

# Local imports
import python_coverage_badge


def build_command_line_interface() -> argparse.ArgumentParser:
    """Builds command line interface for python_coverage_badge package

    Adds the following arguments:
    - Target directory: -d/--directory
    - Target README: -r/--readme
    - Run coverage: -c/--coverage
    - Update badge: -b/--badge

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
        metavar="directory",
        type=str,
        help="Provide path to README.md relative to directory provided.",
    )
    parser.add_argument(
        "-c",
        "--coverage",
        action="store_true",
        help="Run the python coverage package the executes unit tests and generates coverage summary.",
    )
    parser.add_argument(
        "-b",
        "--badge",
        action="store_true",
        help="Update the coverage badge in README.md.",
    )

    return parser
