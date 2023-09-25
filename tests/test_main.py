# Load packages
import unittest  # running tests
from pathlib import Path  # handling file paths

# Local imports
from coverage_shield import (
    __main__,
)  # functions for running coverage


class TestMain(unittest.TestCase):
    def test_main(self):

        # Testing that sending --help parameter into main causes system exit (after printing help message)
        with self.assertRaises(SystemExit):
            __main__.main(["--help"])


if __name__ == "__main__":
    unittest.main()
