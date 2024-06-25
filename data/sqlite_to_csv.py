import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('/Users/eshochat/Downloads/Olim/Olims.db')
cursor = conn.cursor()

# Execute a query to select all data from the combined table
cursor.execute("SELECT * FROM combined_table")

# Fetch all rows from the query result
rows = cursor.fetchall()

# Get the column names from the cursor description
column_names = [description[0] for description in cursor.description]

# Specify the output CSV file
output_csv = 'combined_table.csv'

# Open the CSV file for writing
with open(output_csv, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the column headers to the CSV file
    writer.writerow(column_names)

    # Write the rows to the CSV file
    writer.writerows(rows)

# Close the cursor and connection
cursor.close()
conn.close()

print(f"Data exported successfully to {output_csv}")
