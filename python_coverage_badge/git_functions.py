# Load required libraries
import subprocess  # command line commands
from pathlib import Path  # handling file paths


def check_if_file_changed_using_git(file_path: Path) -> bool:
    """Use git to check if file provided has changed in repo

    Args:
        file_path (Path): path to file that want to check

    Raises:
        subprocess.CalledProcessError: throws error if git status command fails

    Returns:
        bool: True if files have changed and False otherwise
    """
    # Run git status command
    command_result = send_command(
        "git", "status", str(file_path), capture_output=True, text=True
    )

    # Check if ran ok
    if command_result.returncode == 0:  # Passing

        # Check if there is anything to commit
        if "nothing to commit" in command_result.stdout:
            return False
    else:
        raise subprocess.CalledProcessError(
            returncode=command_result.returncode,
            cmd=command_result.args,
            output=command_result.stdout,
            stderr=command_result.stderr,
        )

    # If got to here there must be changes to commit
    return True


# TODO run python -m python_coverage_badge --git_push to test
def push_updated_readme(
    readme_path: Path = Path("README.md"), commit_and_push: bool = True
):
    """Uses git to stage, commit, and push changes to README.md (updated badge)

    Args:
        readme_path (Path, optional): path to README.md file. Defaults to Path("README.md").
        commit_and_push (bool, optional): whether to push changes or not. Defaults to True.
    """

    # Check if updated README changed
    if check_if_file_changed_using_git(readme_path):

        # Convert file path to string
        readme_path_str = str(readme_path)

        # Stage the changes (updated badge)
        send_command("git", "add", readme_path_str)

        # Check if committing and pushing
        if commit_and_push:

            # Commit changes
            commit_message = f"Updated coverage badge in {readme_path}"
            send_command("git", "commit", "-m", commit_message)

            # Push changes
            send_command("git", "push")


def send_command(*args, **kwargs):
    """Send a command in the terminal

    Uses subprocess.run(). Note by default sets check to True to
    check if command runs without failing.

    Args:
        command ([str]): command to run in terminal
        *args: additional commands to send to subprocess.run()
    """

    # Run the command
    result = subprocess.run(args, check=True, **kwargs)
    return result
