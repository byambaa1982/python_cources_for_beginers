import pandas as pd
import sqlite3

# Load the Titanic dataset into a DataFrame
df = pd.read_csv('titanic.csv')

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('titanic.sqlite')

# Write the DataFrame to the 'titanic' table in the SQLite database
df.to_sql('titanic', conn, if_exists='replace', index=False)

# Close the connection to the SQLite database
conn.close()

print("Data has been ingested into the 'titanic' table in titanic.sqlite.")
