# Load packages
from pathlib import Path  # handling file paths

# Local imports
from python_coverage_badge import (
    unittest_coverage_functions,
)  # functions for running coverage

# TODO update to change badge when unittests fail - red "failing" instead of value?
# TODO add more colour categories to scale
# TODO add command line interface


def main():

    # Run code coverage
    coverage_dataframe = unittest_coverage_functions.run_code_coverage()

    # Build badge
    coverage_badge_url = unittest_coverage_functions.make_coverage_badge_url(
        coverage_dataframe
    )

    # Update badge in README
    unittest_coverage_functions.replace_regex_in_file(
        file_path=Path("README.md"),
        pattern_regex=r"\!\[Code Coverage\]\(.+\)",
        replacement=f"![Code Coverage]({coverage_badge_url})",
    )


if __name__ == "__main__":
    main()
