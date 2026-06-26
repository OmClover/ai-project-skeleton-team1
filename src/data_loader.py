import csv
import os

def load_csv(filepath):
    """
    Reads a CSV file and converts its rows into a list of dictionaries.
    
    :param filepath: str, the path to the target CSV file
    :return: list of dict, where each dictionary represents a row (column_name: value)
    :raises FileNotFoundError: if the specified file does not exist
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file at {filepath} was not found.")
        
    records = []
    with open(filepath, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(dict(row))
            
    return records