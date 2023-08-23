# Load packages
import unittest  # running tests
from pathlib import Path  # handling file paths

# Local imports
from python_coverage_badge import (
    git_functions,
)  # functions foir interacting with git


# TODO add tests


class TestGitFunctions(unittest.TestCase):
    def test_check_if_file_changed_using_git(self):

        # Create a temporary file
        temporary_file_path = Path("test_git_file_changed.txt")
        file_lines = ["I", "am", "a", "really", "simple", "file", "\n"]
        with open(temporary_file_path, "w") as file:
            file.write("\n".join(file_lines))

        # Check whether file changed by git
        self.assertTrue(
            git_functions.check_if_file_changed_using_git(temporary_file_path),
            "Check file changed recognised by git",
        )

        # Remove temporary file
        Path.unlink(temporary_file_path)


if __name__ == "__main__":
    unittest.main()
