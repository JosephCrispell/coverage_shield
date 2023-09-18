# Load packages
import unittest  # running tests
from pathlib import Path  # handling file paths
import seaborn  # creating colour palette

# Local imports
from python_coverage_badge import (
    unittest_coverage_functions,
)  # functions for running coverage


class TestUnittestCoverageFunctions(unittest.TestCase):
    def test_replace_regex_in_file(self):
        """Test replacing of pattern in file with string"""

        # Create temporary file
        temporary_file_path = Path("test_README.md")
        file_lines = ["I", "am", "a", "really", "simple", "file", "\n"]
        with open(temporary_file_path, "w") as file:
            file.write("\n".join(file_lines))

        # Replace string in temporary file
        unittest_coverage_functions.replace_regex_in_file(
            file_path=temporary_file_path, pattern_regex=r"s.m.+e", replacement="great"
        )

        # Read in temporary file lines
        file_lines = []
        with open(temporary_file_path) as file:
            file_lines = file.read().splitlines()

        # Check temporary file lines have changed
        self.assertEqual(
            file_lines[4],
            "great",
            "Check string was replaced in file",
        )

        # Remove temporary file
        Path.unlink(temporary_file_path)

    def test_parse_coverage_report(self):
        """Test parse of coverage byte string into coverage report"""

        # Create dummy coverage report data in string
        report_string = "Name                                        Stmts   Miss  Cover\n---------------------------------------------------------------\nsetup.py                                        3      3     0%\ntests/__init__.py                               1      0   100%\ntests/test_data_functions.py                   19      1    95%\ntests/test_timesheet.py                        46      1    98%\ntests/test_unittest_coverage_functions.py      13      1    92%\ntimesheet/__init__.py                           2      0   100%\ntimesheet/data_functions.py                    32      2    94%\ntimesheet/timesheet.py                         53      1    98%\ntimesheet/unittest_coverage_functions.py       41     23    44%\nupdate_test_coverage_badge.py                   8      8     0%\n---------------------------------------------------------------\nTOTAL                                         218     40    82%\n"

        # Parse the report byte string
        coverage_dataframe = unittest_coverage_functions.parse_coverage_report(
            report_string
        )

        # Check dataframe returned
        self.assertEqual(
            str(type(coverage_dataframe)),
            "<class 'pandas.core.frame.DataFrame'>",
            "Check start_time column contains datetimes",
        )

        # Check correct columns are present
        column_names = ["Name", "Stmts", "Miss", "Cover"]
        self.assertTrue(
            all(
                [
                    column_name in coverage_dataframe.columns
                    for column_name in column_names
                ]
            ),
            "Check expected columns present after parsing coverage report",
        )

        # Check some selected values
        self.assertEqual(
            coverage_dataframe.Cover[1],
            float("100.0"),
            "Check second value in Cover column",
        )
        self.assertEqual(
            coverage_dataframe.Name[2],
            "tests/test_data_functions.py",
            "Check third value in Name column",
        )
        self.assertEqual(
            coverage_dataframe.Stmts[7],
            float("53.0"),
            "Check eighth value in Stmts column",
        )

    def test_make_coverage_badge_url(self):
        """Test that shields io coverage badge url created correctly"""

        # Create dummy coverage report data in string
        report_string = "Name                                        Stmts   Miss  Cover\n---------------------------------------------------------------\nsetup.py                                        3      3     0%\ntests/__init__.py                               1      0   100%\ntests/test_data_functions.py                   19      1    95%\ntests/test_timesheet.py                        46      1    98%\ntests/test_unittest_coverage_functions.py      13      1    92%\ntimesheet/__init__.py                           2      0   100%\ntimesheet/data_functions.py                    32      2    94%\ntimesheet/timesheet.py                         53      1    98%\ntimesheet/unittest_coverage_functions.py       41     23    44%\nupdate_test_coverage_badge.py                   8      8     0%\n---------------------------------------------------------------\nTOTAL                                         218     40    82%\n"

        # Parse the report byte string
        coverage_dataframe = unittest_coverage_functions.parse_coverage_report(
            report_string
        )

        # Create badge url
        badge_url = unittest_coverage_functions.make_coverage_badge_url(
            coverage_dataframe
        )

        # Note expected badge colour
        palette = list(seaborn.color_palette("RdYlGn", 100).as_hex())
        coverage_value = 81.7
        badge_colour = palette[round(coverage_value) - 1]

        # Check url
        self.assertEqual(
            badge_url,
            f"https://img.shields.io/badge/coverage-{coverage_value}%25-{badge_colour[1:]}",
            "Check expected shields io badger url produced",
        )

    def test_get_badge_colour(self):
        """Test that correct badger colour returned"""

        # Note expected badge colours
        palette = list(seaborn.color_palette("RdYlGn", 100).as_hex())
        coverage_values = [0, 1, 10, 50, 81.7, 99.1, 100]
        value_colour_indices = [
            round(value) - 1 if value >= 0.5 else 0 for value in coverage_values
        ]
        badge_colours = [palette[index] for index in value_colour_indices]

        # Check badge colour for different values
        for value, colour in zip(coverage_values, badge_colours):

            self.assertEqual(
                colour,
                unittest_coverage_functions.get_badge_colour(value=value),
                f"Checking getting badge colour for value = {value} (should be {colour})",
            )

    def test_load_patterns_to_ignore_in_coverage(self):

        # Create temporary file
        temporary_file_path = Path("test.covignore")
        file_lines = [
            "ignore",
            "\n",
            "# Ignore this comment",
            "\n",
            "this",
            "\n",
            "pattern",
            "\n",
        ]
        with open(temporary_file_path, "w") as file:
            file.write("\n".join(file_lines))

        # Load the patterns from temp file
        patterns = unittest_coverage_functions.load_patterns_to_ignore_in_coverage(
            file_path=temporary_file_path
        )

        # Check patterns loaded correctly
        self.assertEqual(
            patterns[0],
            "ignore",
            "Check pattern read in",
        )
        self.assertEqual(
            patterns[1],
            "this",
            "Check pattern read in",
        )
        self.assertEqual(
            patterns[2],
            "pattern",
            "Check pattern read in",
        )
        self.assertEqual(
            len(patterns),
            3,
            "Check correct number of patterns loaded",
        )

        # Remove temporary file
        Path.unlink(temporary_file_path)


if __name__ == "__main__":
    unittest.main()
