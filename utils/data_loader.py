# utils/data_loader.py
import csv
import json
import pandas as pd

def load_csv_data(file_path):
    """Load test data from a CSV file."""
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [(int(row['user_id']), int(row['expected_status']), int(row['expected_id']) if row['expected_id'] else None) for row in reader]

def load_json_data(file_path):
    """Load test data from a JSON file."""
    with open(file_path) as jsonfile:
        data = json.load(jsonfile)
        return [(item['user_id'], item['expected_status'], item.get('expected_id')) for item in data]

def load_excel_data(file_path, sheet_name='Sheet1'):
    """Load test data from an Excel file."""
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return [(row['user_id'], row['expected_status'], row['expected_id']) for index, row in df.iterrows()]