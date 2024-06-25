import sqlite3
import pandas as pd
import os 
from pathlib import Path

current_dir = Path.cwd()

data_dir = current_dir / 'data'
csv_files = [f for f in data_dir.glob('*.csv')]

def csv_to_sqlite(db_name, files):
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    for file in csv_files:
        try:
            # Try reading with 'utf-8' encoding
            df = pd.read_csv(file, encoding='utf-8')
        except UnicodeDecodeError as e:
            print(f"Error reading {file} with 'utf-8' encoding: {e}")
            print("Trying with 'cp1255' encoding...")
            try:
                # Try reading with 'cp1255' encoding
                df = pd.read_csv(file, encoding='cp1255')
            except UnicodeDecodeError as e:
                print(f"Error reading {file} with 'cp1255' encoding: {e}")
                print("Trying with 'utf-16' encoding...")
                try:
                    # Try reading with 'utf-16' encoding
                    df = pd.read_csv(file, encoding='utf-16')
                except Exception as e:
                    print(f"Failed to read {file} with 'utf-16' encoding: {e}")
                    continue

        # Get table name from file name (without extension)
        table_name = os.path.splitext(os.path.basename(file))[0]

        # Write the data to the SQLite table
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Table '{table_name}' created successfully.")

    # Close the connection
    conn.close()


# List of CSV files
files = ['2015.csv', '2016.csv', '2017.csv', '2018.csv', '/2019.csv', '2020.csv', '2021.csv', '2022.csv', '2023.csv']

# Name of the SQLite database
db_name = 'Olims.db'

# Convert CSV files to SQLite
csv_to_sqlite(db_name, csv_files)
