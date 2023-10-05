# Load required libraries
import subprocess  # command line commands
import coverage  # not used directly but run in command line
from io import StringIO  # reading byte string (returned by coverage)
import pandas as pd  # working with dataframes
from pathlib import Path  # handling file paths
import re  # working with regular expressions
import warnings  # send warnings
import seaborn  # create colour palette


def parse_coverage_report(
    coverage_report_string: str, patterns_to_ignore: [str] = None
) -> pd.DataFrame:
    """Parses byte string returned by coverage report into pandas dataframe

    Args:
        coverage_report_string (bytes): string version of coverage report

    Returns:
        pd.DataFrame: coverage report as dataframe
    """

    # Convert the byte string into pandas dataframe
    coverage_dataframe = pd.read_csv(StringIO(coverage_report_string), sep="\s+")

    # Remove empty rows
    coverage_dataframe = coverage_dataframe[1:-2]
    coverage_dataframe = coverage_dataframe.reset_index(drop=True)

    # Remove percent sign from coverage column and convert to float
    coverage_dataframe.Cover = coverage_dataframe.Cover.str[:-1].astype(float)

    # Check if any patterns to ignore
    if not patterns_to_ignore == None:
        patterns_to_ignore = "|".join(patterns_to_ignore)
        coverage_dataframe = coverage_dataframe[
            ~coverage_dataframe.Name.str.contains(patterns_to_ignore)
        ]

    return coverage_dataframe


def run_code_coverage(tester: str = "unittest") -> pd.DataFrame:
    """Runs coverage tool in command line and returns report

    Will send warning if running coverage package is failing and return empty dataframe

    Returns:
        pd.DataFrame : coverage report as dataframe if coverage passing; empty dataframe if coverage failing
    """

    # Check tester option provided
    tester_options = ["unittest", "pytest"]
    if not tester in tester_options:
        raise ValueError(f"The tester option provided ({tester}) was not recognised. Must be one of: {tester_options.join(', ')}")

    # Run code coverage calculation
    # Check out useful subprocess function docs: https://www.datacamp.com/tutorial/python-subprocess
    coverage_command = [
        "python3",
        "-m",
        "coverage",
        "run",
        "--source=.",
        "-m",
        tester,
    ]
    command_result = subprocess.run(coverage_command, capture_output=True, text=True)

    # Check the result
    if command_result.returncode == 0:  # Passing

        # Show result from command
        # - For some reason unit testing progress sent to standard error
        # - Any prints from unit tests sent to standard output so ignoring these for the moment
        print(command_result.stderr)

        # Generate the report
        report_command = ["python3", "-m", "coverage", "report"]
        try:
            coverage_report = subprocess.check_output(report_command, text=True)

        except subprocess.CalledProcessError as error:
            print(
                f"Generating coverage report command ({' '.join(report_command)}) failed! Return code: {error.returncode}"
            )

        # Get patterns to ignore
        patterns_to_ignore = load_patterns_to_ignore_in_coverage()

        # Convert coverage report output to dataframe
        report_dataframe = parse_coverage_report(coverage_report, patterns_to_ignore)

    else:
        warnings.warn(
            f"Running coverage package command ({' '.join(coverage_command)}) failed! Return code: {command_result.returncode}. \nError Output:\n{command_result.stderr}"
        )

        report_dataframe = pd.DataFrame()

    return report_dataframe


def get_badge_colour(
    value: float,
    colour_palette: str = "RdYlGn",
) -> str:
    """Gets coverage badger colour based on value and thresholds

    Args:
        value (float): coverage value
        colour_palette (str): name of colour palette to use (see: https://holypython.com/python-visualization-tutorial/colors-with-python/)

    Returns:
        str: colour for badge
    """

    # Create colour palette
    # Note shields io accepts hex colours (without hash!)
    # (as well as many other formats! https://shields.io/badges)
    palette = list(seaborn.color_palette(colour_palette, 100).as_hex())

    # Get colour for value
    value_index = round(value) - 1 if value >= 0.5 else 0
    badge_colour = palette[value_index]

    return badge_colour


def make_coverage_badge_url(
    coverage_dataframe: pd.DataFrame | str,
    failing_colour: str = "red",
) -> str:
    """Uses shields io to build coverage badge

    Args:
        coverage_dataframe (pd.DataFrame | str): coverage report as dataframe. If coverage failed this will be string ("failing")
        failing_colour (str, optional): colour of badge when failing. Defaults to "red".

    Returns:
        str: shields io badge url
    """

    # Check if coverage report available
    if not coverage_dataframe.empty:

        # Calculate the average code coverage
        total_statements = sum(coverage_dataframe.Stmts)
        total_statements_missed = sum(coverage_dataframe.Miss)
        average_coverage = (
            total_statements - total_statements_missed
        ) / total_statements

        # Convert to percentage and round
        average_coverage = round(average_coverage * 100, 1)

        # Note badger colour
        badge_colour = get_badge_colour(average_coverage)

        # Build badge
        badge_url = f"https://img.shields.io/badge/coverage-{average_coverage}%25-{badge_colour[1:]}"

    else:

        # Build badge
        badge_url = f"https://img.shields.io/badge/coverage-failing-{failing_colour}"

    return badge_url


def replace_regex_in_file(
    file_path: Path, pattern_regex: str, replacement: str, add_to_file: bool = True
):
    """Replace pattern in file with string

    Note if pattern not present this will add string to first line by default

    Args:
        file_path (Path): path to file
        pattern_regex (str): pattern to find
        replacement (str): string to replace pattern when found
        add_to_file (bool): if regex not present will add to top of file if True. Defaults to True
    """

    # Read in file contents
    file_lines = []
    with open(file_path) as file:
        file_lines = file.read().splitlines()

    # Check if badge present
    badge_present = any(bool(re.match(pattern_regex, line)) for line in file_lines)
    if (badge_present == False) & add_to_file:
        # If not add at top
        file_lines.insert(0, replacement)

    else:
        # If it is, update
        file_lines = [re.sub(pattern_regex, replacement, line) for line in file_lines]

    # Write file lines back to file
    with open(file_path, "w") as file:
        file.write("\n".join(file_lines) + "\n")


def load_patterns_to_ignore_in_coverage(file_path: Path = Path(".covignore")) -> [str]:
    """Loads patterns from simple text file lines into list

    Note file is like .gitignore so each line represents a pattern to ignore. Commented lines
    can start with hash (#) and empty lines are ignored.
    Args:
        file_path (Path): path to file containing patterns

    Returns:
        [list] : list of patterns to ignore
    """

    # Check if file exists
    if file_path.is_file():

        # Get the file lines from the file
        file_lines = []
        with open(file_path) as file:
            file_lines = file.read().splitlines()

        # Ignore comment or empty lines
        file_lines = [line for line in file_lines if not line.startswith("#")]

        # Remove empty values
        file_lines = list(filter(None, file_lines))

        # Check if no lines present
        file_lines = None if len(file_lines) == 0 else file_lines

        return file_lines

    else:
        return None
