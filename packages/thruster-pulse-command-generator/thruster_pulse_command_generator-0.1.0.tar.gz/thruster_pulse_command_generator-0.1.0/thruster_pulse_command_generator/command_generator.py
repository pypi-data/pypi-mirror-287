import os
import re
import yaml
import pandas as pd
from spc_toolkit.utils.commands import Command, CommandConfiguration
from spc_toolkit.utils.command_parameters import Parameter
from typing import List, Dict, Optional, Union

def import_mission_config(mission_config_path: str) -> CommandConfiguration:
    """
    Imports the mission configuration from the specified path. 

    Args:
        mission_config_path (str): The path to the mission configuration directory.

    Returns:
        CommandConfiguration: An instance of CommandConfiguration with the loaded configuration.
    """
    commands_config = CommandConfiguration()
    if mission_config_path:
        commands_config_path = os.path.join(mission_config_path, 'commands.toml')
        if os.path.exists(commands_config_path):
            commands_config = CommandConfiguration(commands_config_path)
    
    return commands_config 

def extract_number_from_column(column_name: str) -> Optional[int]:
    """
    Extracts a numerical value from a column name if it matches the pattern 'Thr(\d+)'.

    Args:
        column_name (str): The name of the column from which to extract the number.

    Returns:
        int or None: The extracted number if found, otherwise None.
    """
    pattern = r'Thr(\d+)'
    match = re.search(pattern, column_name)
    
    if match:
        number = match.group(1)
        return int(number)
    else:
        return None

def normalize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalizes the column names of the DataFrame by removing spaces and stripping extra whitespace.

    Args:
        df (pd.DataFrame): The DataFrame whose column names need normalization.

    Returns:
        pd.DataFrame: The DataFrame with normalized column names.
    """
    df.columns = df.columns.str.strip().str.replace(' ', '')
    return df

def calculate_time_difference(df: pd.DataFrame, index: int) -> int:
    """
    Calculates the time difference in milliseconds between the current and previous rows.

    Args:
        df (pd.DataFrame): The DataFrame containing the time column.
        index (int): The index of the current row.

    Returns:
        int: The time difference in milliseconds.
    """
    if index == 0:
        return int(round(df['Time'].iloc[index] * 1000))
    else:
        current_time = df['Time'].iloc[index]
        previous_time = df['Time'].iloc[index - 1]
        return int(round((current_time - previous_time) * 1000))

def build_param_values(init_state_df_thr: pd.DataFrame, row_init_state: pd.Series, row_first_edge: pd.Series, 
                       row_second_edge: pd.Series, field_names: List[str]) -> List[Dict[str, int]]:
    """
    Builds parameter values for the command based on the data from the DataFrames.

    Args:
        init_state_df_thr (pd.DataFrame): The DataFrame with initial state thruster data.
        row_init_state (pd.Series): The series corresponding to the current row of initial state data.
        row_first_edge (pd.Series): The series corresponding to the current row of first edge data.
        row_second_edge (pd.Series): The series corresponding to the current row of second edge data.
        field_names (List[str]): List of field names for the command parameters.

    Returns:
        List[Dict[str, int]]: A list of dictionaries, each containing parameter values for a thruster.
    """
    values_list = []
    for col in init_state_df_thr.columns:
        thruster_num = extract_number_from_column(col)
        if thruster_num and thruster_num > 0:
            address = thruster_num - 1
        else:
            address = 0 # Default
              
        start_on = row_init_state[col]
        edge_1 = row_first_edge[col]
        edge_2 = row_second_edge[col]
        
        params = {
            field_names[0]: address, 
            field_names[1]: int(start_on),
            field_names[2]: int(edge_1),
            field_names[3]: int(edge_2)
        }
        values_list.append(params)
    return values_list

def make_arm_command(commands_config: CommandConfiguration) -> Dict[str, Union[str, List[Dict[str, int]]]]:
    """
    Creates and returns a YAML-compatible dictionary for the Arm command.

    Args:
        commands_config (CommandConfiguration): The command configuration instance.

    Returns:
        Dict[str, Union[str, List[Dict[str, int]]]]: A dictionary representing the Arm command in YAML format.
    """
    command_id = commands_config.get_item('Arm').byte_code
    return Command(command_id=command_id, commands_config=commands_config).to_yaml_dict()

def create_command(commands_config: CommandConfiguration, init_state_df: pd.DataFrame, first_edge_df: pd.DataFrame,
                   second_edge_df: pd.DataFrame) -> List[List[Dict[str, Union[int, List[Dict[str, int]]]]]]:
    """
    Creates and prints a command based on the configuration and data provided.

    Args:
        commands_config (CommandConfiguration): The command configuration instance.
        init_state_df (pd.DataFrame): The DataFrame with initial state thruster data.
        first_edge_df (pd.DataFrame): The DataFrame with first edge thruster data.
        second_edge_df (pd.DataFrame): The DataFrame with second edge thruster data.
    
    Returns:
        List[List[Dict[str, Union[int, List[Dict[str, int]]]]]]: A list where each element is a list containing:
            - A dictionary with a timestep key and its corresponding value.
            - A dictionary representing the command, including a Fire key with a list of thruster parameters.
    """
    # Retrieve command ID and parameter names and sizes from configuration
    command_id = commands_config.get_item('Fire').byte_code
    field_names = commands_config.get_item(command_id).parameter_names
    field_sizes = commands_config.get_item(command_id).parameter_sizes
    
    # Check that the configuration matches expected size
    if len(field_names) != 4:
        return []
    
    # Normalize and filter DataFrames to only include thruster-related columns
    init_state_df_thr = normalize_column_names(init_state_df).filter(like="Thr").copy()
    first_edge_df_thr = normalize_column_names(first_edge_df).filter(like="Thr").copy()
    second_edge_df_thr = normalize_column_names(second_edge_df).filter(like="Thr").copy()
    
    # Create empty list to store all commands
    command_list = []
    
    # Store ARM command
    arm_command_dict = make_arm_command(commands_config)
    
    # Determine the minimum number of rows to iterate over
    min_rows = min(len(init_state_df_thr), len(first_edge_df_thr), len(second_edge_df_thr))    
    for index in range(min_rows):
        row_init_state = init_state_df_thr.iloc[index]
        row_first_edge = first_edge_df_thr.iloc[index]
        row_second_edge = second_edge_df_thr.iloc[index]
        
        # Calculate the time difference for the current row
        time = {'timestep': calculate_time_difference(init_state_df, index)}
        
        # Build parameter values for the command
        values_list = build_param_values(init_state_df_thr, row_init_state, row_first_edge, row_second_edge, field_names)
        
        # Create Parameter instances and build the Command instance
        param_list = [Parameter(field_names=field_names, field_sizes=field_sizes, **values) for values in values_list]
        
        # Create Command instance
        command = Command(command_id=command_id, parameters=tuple(param_list), commands_config=commands_config)
        command_dict = command.to_yaml_dict()
        
        # If it's been longer than 60s or if this is the beginning of the command sequence, add an ARM command
        if index == 0 or init_state_df['Time'].iloc[index] / 60 == 0:
            command_list.append([{'timestep': 0}, arm_command_dict])
        
        # Append full command to command list
        command_list.append([time, command_dict])
    
    return command_list     

def load_sheet_by_keyword(excel_file: str, keyword: str) -> Optional[pd.DataFrame]:
    """
    Loads a DataFrame from an Excel file where the sheet name contains the specified keyword.

    Args:
        excel_file (str): Path to the Excel file.
        keyword (str): Substring to search for in sheet names.

    Returns:
        pd.DataFrame or None: DataFrame corresponding to the sheet containing the keyword, or None if not found.
    """
    xls = pd.ExcelFile(excel_file)
    for sheet_name in xls.sheet_names:
        if keyword in sheet_name:
            return pd.read_excel(excel_file, sheet_name=sheet_name)
    return None

def generate_command_yaml(excel_file, mission_config_path, yaml_file_name, individual_filenames) -> None:
    """
    Main function to load data from an Excel file, import configuration, and create commands.
    """
    # Load the DataFrames from Excel file sheets based on keywords
    init_state_df = load_sheet_by_keyword(excel_file, individual_filenames[0])
    first_edge_df = load_sheet_by_keyword(excel_file, individual_filenames[1])
    second_edge_df = load_sheet_by_keyword(excel_file, individual_filenames[2])
    
    # Import mission configuration and create commands
    mission_config = import_mission_config(mission_config_path)
    command_list = create_command(mission_config, init_state_df, first_edge_df, second_edge_df)
    
    # Generate YAML content
    yaml_content = yaml.dump(command_list, default_flow_style=False)
    
    # Apply formatting for new commands
    formatted_yaml = yaml_content.replace('- -', '\n-\n  -')
    
    # Get the base name of the Excel file and change the extension to '.yaml'
    base_name = os.path.basename(excel_file)
    
    if yaml_file_name is None:
        yaml_file_name = os.path.splitext(base_name)[0] + '.yaml'
    
    # Write formatted YAML content to file
    with open(yaml_file_name, 'w') as file:
        file.write(formatted_yaml)