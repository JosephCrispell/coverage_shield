# Load packages
import unittest  # running tests
from pathlib import Path  # handling file paths
import subprocess  # command line commands

# Local imports
from python_coverage_badge import (
    git_functions,
)  # functions for interacting with git


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

    def test_push_updated_readme(self):

        # Create a temporary file
        temporary_file_path = Path("test_git_file_changed.txt")
        file_lines = ["I", "am", "a", "really", "simple", "file", "\n"]
        with open(temporary_file_path, "w") as file:
            file.write("\n".join(file_lines))

        # Commit changed file
        git_functions.push_updated_readme(
            readme_path=temporary_file_path, commit_and_push=False
        )

        # Check whether file changed by git
        command_result = git_functions.send_command(
            "git", "status", capture_output=True, text=True
        )

        # Check if there is anything to commit
        self.assertTrue(
            str(temporary_file_path) in command_result.stdout,
            "Check changed file staged",
        )

        # Reset git
        command_result = git_functions.send_command(
            "git", "reset", str(temporary_file_path)
        )

        # Remove temporary file
        Path.unlink(temporary_file_path)

    def test_send_command(self):

        # Send a command in terminal
        statement = "hello"
        command_result = git_functions.send_command(
            "echo", f'"{statement}"', capture_output=True, text=True
        )

        # Check the command result
        self.assertTrue(
            statement in command_result.stdout, "Check sending command in terminal"
        )


if __name__ == "__main__":
    unittest.main()
