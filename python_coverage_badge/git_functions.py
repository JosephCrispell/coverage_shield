# Load required libraries
import subprocess  # command line commands
from pathlib import Path  # handling file paths


def push_updated_readme(readme_path: Path = Path("README.md")):
    """Uses git to stage, commit, and push changes to README.md (updated badge)

    Args:
        readme_path (Path, optional): path to README.md file. Defaults to Path("README.md").
    """

    # Stage the changes (updated badge)
    stage_file(readme_path)

    # Commit changes
    commit_changes(message=f"Updated coverage badge in {readme_path}")

    # Push changes
    push_changes()


def run_command_without_collecting_output(command: list[str]):
    """Runs command in the command line (terminal)

    Args:
        command (list[str]): command to run

    Raises:
        subprocess.CalledProcessError: throws error if command fails
    """

    # Run the command
    command_result = subprocess.run(command, capture_output=True, text=True)

    # Check command ran ok
    if command_result != 0:

        raise subprocess.CalledProcessError(
            f"Command provided ({' '.join(command)}) failed with code: {command_result.returncode}. Error message:\n\n{command_result.stderr}"
        )


def stage_file(file_path: Path):
    """Use git to stage file

    Args:
        file_path (Path): path to file to stage
    """

    # Build the command to stage file
    staging_command = ["git", "add", repr(file_path)]

    # Run the command
    run_command_without_collecting_output(staging_command)


def commit_changes(message: str):
    """Use git to commit changes made

    Raises:
        subprocess.CalledProcessError: throws error if command to commit changes fails
    """

    # Build the command to commit changes
    commit_command = ["git", "commit", "-m", message]

    # Run the command
    run_command_without_collecting_output(commit_command)


def push_changes(message: str):
    """Use git to push committed changes

    Raises:
        subprocess.CalledProcessError: throws error if command to push committed changes fails
    """

    # Build the command to push changes
    push_command = [
        "git",
        "push",
    ]

    # Run the command
    run_command_without_collecting_output(push_command)
