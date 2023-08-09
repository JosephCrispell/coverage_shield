# Local imports
from python_coverage_badge import (
    command_line_interface_functions,
)  # functions for running coverage

# TODO add more colour categories to scale
# TODO add unittest for main
# TODO update to run git


def main():

    # Build interface
    parser = command_line_interface_functions.build_command_line_interface()

    # Parse arguments
    command_line_interface_functions.parse_command_line_arguments(parser)


if __name__ == "__main__":
    main()
