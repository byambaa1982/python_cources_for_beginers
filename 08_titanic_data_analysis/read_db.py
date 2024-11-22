import pandas as pd
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('titanic.sqlite')

# Read the 'titanic' table into a pandas DataFrame
df = pd.read_sql('SELECT * FROM titanic', conn)

# Close the connection to the SQLite database
conn.close()

# Display the DataFrame
print(df.head())  # To print the first few rows of the DataFrame
