"""Command line interface for the thruster-pulse-command-generator.

This CLI allows you to generate a YAML file containing fire commands for Stellar Exploration missions from an
Excel file (.xlsx) that includes information on start times, edge 1, and edge 2, as well as from a mission configuration
directory. It is designed to be used from the command line and provides a straightforward way to handle mission configuration
files and parameter data.
"""

import argparse
from pathlib import Path
import sys
import yaml

from thruster_pulse_command_generator.command_generator import generate_command_yaml


def _cli_arg_parser():
    """Creates the parser used by the thruster-pulse-command-generator command-line tool."""
    parser = argparse.ArgumentParser(
        prog="thruster_pulse_command_generator",
        description="""Generate YAML files for Fire commands based on mission configuration and parameter data from .xlsx files."""
    )

    parser.add_argument(
        "-C",
        "--config",
        type=str,
        metavar="path",
        required=True,
        help="""Path to the mission configuration directory."""
    )
    
    parser.add_argument(
        "-P",
        "--param-xlsx",
        type=str,
        metavar="path",
        required=True,
        help="""Path to the .xlsx file containing tabs for start_on, edge_1, and edge_2."""
    )

    parser.add_argument(
        "-F",
        "--yaml-filename",
        type=str,
        metavar="filename",
        required=False,
        default=None,
        help="""Specify the output filename for the YAML file. If not provided, the output filename will be derived from the .xlsx file."""
    )

    parser.add_argument(
        "-I",
        "--individual-filenames",
        type=str, 
        nargs='+',
        metavar="filename",
        required=False,
        default=None,
        help="""Specify individual filenames for sheets in the .xlsx file. Defaults are 'initState', 'firstEdge', and 'secondEdge'."""
    )

    return parser

def main():
    """Main CLI entry point."""
    parser = _cli_arg_parser()
    args = parser.parse_args()

    # Extract arguments
    config_path = args.config
    param_xlsx_path = args.param_xlsx
    yaml_filename = args.yaml_filename
    individual_filenames = args.individual_filenames

    # Print help if arguments are missing or incorrect
    if not all([config_path, param_xlsx_path]):
        parser.print_help()
        sys.exit(1)
        
    if not individual_filenames or len(individual_filenames) < 3:
        individual_filenames = ['initState', 'firstEdge', 'secondEdge']

    # Call the main function from command_generator.py with the parsed arguments
    generate_command_yaml(param_xlsx_path, config_path, yaml_filename, individual_filenames)

if __name__ == "__main__":
    main()