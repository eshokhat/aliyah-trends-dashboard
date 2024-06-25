import pandas as pd
import matplotlib.pyplot as plt

combined_table_path = '/Users/eshochat/Downloads/Olim/combined_table.csv'

def top_district():
    try:
        # Load data from the CSV file
        df = pd.read_csv(combined_table_path)
        
        # Group by country and count number of olims, then select top 10 countries
        grouped_data = df.groupby('machoz').size().reset_index(name='olims')
        grouped_data = grouped_data.sort_values(by='olims', ascending=False).head(10)
        
        # Extracting data into separate lists for plotting
        countries = grouped_data['machoz'].tolist()
        olims = grouped_data['olims'].tolist()
        
        # Create a bar plot using matplotlib
        plt.figure(figsize=(12, 6))
        plt.bar(countries, olims)
        plt.xlabel('Districts')
        plt.ylabel('Olims')
        plt.title('Top Districts by Olims')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print(f"File '{combined_table_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
