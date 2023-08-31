# Load packages
import sys  # accessing command line arguments

# Local imports
from python_coverage_badge import (
    command_line_interface_functions,
)  # functions for running coverage

# TODO add more colour categories to scale


def main(arguments: list[str] = sys.argv[1:]):

    # Build interface
    parser = command_line_interface_functions.build_command_line_interface()

    # Parse arguments
    command_line_interface_functions.parse_command_line_arguments(
        parser, arguments=arguments
    )


if __name__ == "__main__":
    main()
