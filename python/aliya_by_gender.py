import matplotlib.pyplot as plt
import pandas as pd
import logging

logger = logging.getLogger(__name__)
combined_table_path = '/Users/eshochat/Downloads/Olim/combined_table.csv'

def aliya_by_gender():
    try:
        # Load data from the CSV file
        df = pd.read_csv(combined_table_path)
        
        # Check if data is empty
        if df.empty:
            print("No data found")
            return
        
        # Grouping the data by year and gender and counting the number of olims
        grouped_data = df.groupby(['year_aliya', 'gender']).size().reset_index(name='olims')
        
        # Separate data for each gender
        male_data = grouped_data[grouped_data['gender'] == 'male']
        female_data = grouped_data[grouped_data['gender'] == 'female']
        
        # Extracting years and counts for males and females
        years_male = male_data['year_aliya'].tolist()
        counts_male = male_data['olims'].tolist()
        years_female = female_data['year_aliya'].tolist()
        counts_female = female_data['olims'].tolist()
        
        # Creating a bar plot using matplotlib
        plt.figure(figsize=(12, 6))
        
        # Plotting bar charts for males and females side by side
        plt.bar([year - 0.2 for year in years_male], counts_male, width=0.4, align='center', label='Male', color='blue')
        plt.bar([year + 0.2 for year in years_female], counts_female, width=0.4, align='center', label='Female', color='red')
        
        # Adding labels and title
        plt.xlabel('Year')
        plt.ylabel('Number of Olims')
        plt.title('Number of Olims per Year and Gender')
        plt.xticks(range(min(min(years_male), min(years_female)), max(max(years_male), max(years_female)) + 1))
        plt.legend()
        
        # Display the plot
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        logger.error(f"An error occurred: {e}")
