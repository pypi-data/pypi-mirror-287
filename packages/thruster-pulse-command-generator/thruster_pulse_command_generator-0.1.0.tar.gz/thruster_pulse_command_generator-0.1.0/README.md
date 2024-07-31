# Thruster Pulse Command Generator

## Overview

The `thruster-pulse-command-generator` CLI tool is designed to generate YAML files for fire commands used in Stellar Exploration missions. This tool processes an Excel file (.xlsx) containing mission parameters and integrates this data with a mission configuration directory to produce a YAML file. It simplifies the management of mission configurations and parameter data into Fire commands.

## Features

- **Generate YAML Files**: Create YAML files with fire commands based on mission configuration and parameters.
- **Configurable Inputs**: Specify paths for mission configuration, parameter files, and output filenames.
- **Flexible Sheet Naming**: Customize Excel sheet names for different data sections.

## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management and packaging. To set up the project, follow these steps:

1. **Install Poetry** (if you haven't already):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 - 
   ```
2. **Clone the Repository:**
    ```bash
    git clone git@gitlab.com:stellar-exploration/harley/thruster-pulse-command-generator.git
    ```  
3. **cd into the Repository Directory**
4. **Install Dependencies:**
    ```bash
    poetry install
    ```

## Usage

Display thruster-pulse-command-generator CLI usage

```bash
thruster-pulse-command-generator --help
```

You can use this CLI tool from the command line by running the following command:

```bash
thruster-pulse-command-generator -C <path_to_mission_config_directory> -P <path_to_param_xlsx_file> [-F <output_yaml_filename>] [-I <sheet_name1> <sheet_name2> <sheet_name3>]
```

### Arguments

- `-C`, `--config`
  - **Required**: Path to the mission configuration directory.

- `-P`, `--param-xlsx`
  - **Required**: Path to the Excel file (.xlsx) containing the mission parameters. This file should include tabs named for start times, edge 1, and edge 2 (or custom names if specified).

- `-F`, `--yaml-filename`
  - **Optional**: Specify the output filename for the generated YAML file. If not provided, the output filename will be derived from the Excel file name.

- `-I`, `--individual-filenames`
  - **Optional**: Provide custom names for the Excel sheet tabs. The default names are `initState`, `firstEdge`, and `secondEdge`.

### Example

To generate a YAML file using default sheet names and a specific output filename, you would run:

```bash
thruster-pulse-command-generator -C /path/to/config -P /path/to/params.xlsx -F output.yaml
```

To use custom sheet names:
```bash
thruster-pulse-command-generator -C /path/to/config -P /path/to/params.xlsx -I customInitState customFirstEdge customSecondEdge
```