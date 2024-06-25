import pandas as pd

combined_table_path = '/Users/eshochat/Downloads/Olim/combined_table.csv'

def settlement_list():
    try:
        df = pd.read_csv(combined_table_path).fillna('No information available')
        return pd.unique(df['yeshuv_klita'].tolist())
    except FileNotFoundError:
        print("Error: Data file not found.")
    except pd.errors.EmptyDataError:
        print("Error: Data file is empty.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
