# Load packages
import unittest  # running tests
from pathlib import Path  # handling file paths

# Local imports
from coverage_shield import command_line_interface_functions  # cli functions


class TestCommandLineInterfaceFunctions(unittest.TestCase):
    def test_build_command_line_interface(self):
        """Test command line parser is built"""

        # Build the command line interface parser
        parser = command_line_interface_functions.build_command_line_interface()

        # Check argument parser returned
        self.assertEqual(
            str(type(parser)),
            "<class 'argparse.ArgumentParser'>",
            "Check argument parser returned",
        )

    def test_parse_command_line_arguments(self):

        # Build the command line interface parser
        parser = command_line_interface_functions.build_command_line_interface()

        # Define the command line arguments and parse
        directory = "test_directory"
        readme = "test_README"
        arguments = [
            "--directory",
            directory,
            "--readme",
            readme,
        ]
        args = command_line_interface_functions.parse_command_line_arguments(
            parser, arguments, testing=True
        )

        # Check args exist
        self.assertEqual(
            directory,
            args.directory,
            "Check directory stored as argument",
        )
        self.assertEqual(
            readme,
            args.readme,
            "Check readme stored as argument",
        )


if __name__ == "__main__":
    unittest.main()
