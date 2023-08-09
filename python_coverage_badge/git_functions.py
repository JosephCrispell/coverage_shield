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


def stage_file(file_path: Path):
    """Use git to stage file

    Args:
        file_path (Path): path to file to stage
    """

    # Build the command to stage file
    staging_command = ["git", "add", str(file_path)]

    # Run the command
    subprocess.run(staging_command, check=True)


def commit_changes(message: str):
    """Use git to commit changes made

    Args:
        message (str): git commit message
    """

    # Build the command to commit changes
    commit_command = ["git", "commit", "-m", message]

    # Run the command
    subprocess.run(commit_command, check=True)


def push_changes():
    """Use git to push committed changes"""

    # Build the command to push changes
    push_command = [
        "git",
        "push",
    ]

    # Run the command
    subprocess.run(push_command, check=True)
