# Load packages
import unittest  # running tests
from pathlib import Path  # handling file paths

# Local imports
from python_coverage_badge import (
    unittest_coverage_functions,
)  # functions for running coverage


class TestMain(unittest.TestCase):
    def test_main(self):

        # TODO Add test in here!
        print("hello! Main test to add!")


if __name__ == "__main__":
    unittest.main()
