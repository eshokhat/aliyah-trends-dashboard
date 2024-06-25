import pandas as pd
import matplotlib.pyplot as plt

combined_table_path = '/Users/eshochat/Downloads/Olim/combined_table.csv'

def aliya_per_month(year_aliya):
    try:
        # Load data from the CSV file
        df = pd.read_csv(combined_table_path)
        
        # Filter data for the specified year
        year_data = df[df['year_aliya'] == year_aliya]
        
        # Group by month and count number of olims
        grouped_data = year_data.groupby('month_aliya').size().reset_index(name='olims')
        
        # Extracting data into separate lists for plotting
        month = grouped_data['month_aliya'].tolist()
        olims = grouped_data['olims'].tolist()
        
        if not month:
            print(f"No data found for year {year_aliya}")
            return
        
        # Create a line plot using matplotlib
        plt.figure(figsize=(12, 6))
        plt.plot(month, olims, marker='o', linestyle='-', color='blue', label='Olims per Month')
        
        # Adding labels and title
        plt.xlabel('Month')
        plt.ylabel('Olims')
        plt.title(f'Olims Distribution for Year {year_aliya} by Month')
        plt.xticks(month)
        plt.legend()
        
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print(f"File '{combined_table_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}");
