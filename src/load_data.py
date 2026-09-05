import numpy as np
import pandas as pd
import os

def load_data(file_path):
    """
    Load data from a Parquet file and return it as a pandas DataFrame.

    Parameters:
    file_path (str): The path to the Parquet file.

    Returns:
    pd.DataFrame: The loaded data as a DataFrame.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    try:
        data = pd.read_parquet(file_path)
        return data
    except Exception as e:
        raise ValueError(f"An error occurred while loading the data: {e}")