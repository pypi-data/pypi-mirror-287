#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 16:59:48 2024

@author: cameronmeharry
"""

import os
import pandas as pd
from importlib import resources

def list_csv_files():
    csv_files = []
    data_path = resources.files('cpykg') / 'data'
    for file in data_path.iterdir():
        if file.suffix == '.csv':
            csv_files.append(file.name)
    return csv_files

def read_csv_file(filename):
    if not filename.endswith('.csv'):
        raise ValueError("File must be a CSV")
    
    data_path = resources.files('cpykg') / 'data'
    file_path = data_path / filename
    
    if not file_path.is_file():
        raise FileNotFoundError(f"No such file: {filename}")
    
    with file_path.open('r') as file:
        df = pd.read_csv(file, index_col=0)
    return df

'''
# Example usage
if __name__ == "__main__":
    csv_files = list_csv_files()
    print("Available CSV files:", csv_files)
    
    for csv_file in csv_files:
        df = read_csv_file(csv_file)
        print(f"Contents of {csv_file}:")
        print(df.head())  # Print first few rows of each CSV
'''