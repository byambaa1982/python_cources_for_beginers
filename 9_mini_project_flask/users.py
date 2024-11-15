import sqlite3
import hashlib

# Connect to the database
conn = sqlite3.connect('titanic.sqlite')
cursor = conn.cursor()

# Create the users table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL)''')

cursor.execute('DROP TABLE contacts')

# Create the contacts table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT  NOT NULL,
                    message TEXT NOT NULL,
                    current_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

# Commit changes and close the connection
conn.commit()
conn.close()
