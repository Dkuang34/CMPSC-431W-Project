import csv
import hashlib
import sqlite3

# Define file names

def sha256hash(password):
    hashed_pw =  hashlib.sha256(password.encode()).hexdigest()
    return hashed_pw

# Connect to (or create) the SQLite database
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Create the USERS table if it doesn't exist
cursor.execute('CREATE TABLE IF NOT EXISTS USERS (email TEXT PRIMARY KEY NOT NULL, password TEXT NOT NULL)')

# Read from CSV and insert rows
with open('Users.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        email = row[0]
        # Hash the password
        hashed_password = sha256hash(row[1])
        # Insert into the USERS table
        cursor.execute('INSERT INTO USERS VALUES (?, ?)', (email, hashed_password))

# Commit the transaction and close the connection
connection.commit()
connection.close()
