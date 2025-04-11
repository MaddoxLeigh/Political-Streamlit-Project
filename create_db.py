import pandas as pd
import sqlite3
import os

# Define paths
data_dir = 'docs/Data'
db_path = os.path.join(data_dir, 'PoliticsandDataSci.db')

# Create database connection
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# List of CSV files and their corresponding table names
csv_tables = {
    'StateData.csv': 'State Data',
    'BidenPolls.csv': 'Biden polls',
    'BidenEvents.csv': 'Biden Events',
    'InteractiveData.csv': 'Interactive Data',
    'UKCrimeRates.csv': 'UK crime rates',
    'LondonCrimeCategories.csv': 'London crime categories',
    'GlobalPopulation.csv': 'Global population',
    'GlobalGini.csv': 'Global gini'
}

# Create tables and import data
for csv_file, table_name in csv_tables.items():
    csv_path = os.path.join(data_dir, csv_file)
    if os.path.exists(csv_path):
        # Read CSV file
        df = pd.read_csv(csv_path)
        
        # Create table
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Created table '{table_name}' from {csv_file}")
    else:
        print(f"Warning: {csv_file} not found in {data_dir}")

# Commit changes and close connection
conn.commit()
conn.close()

print("\nDatabase creation complete!")
print(f"Database file created at: {db_path}") 