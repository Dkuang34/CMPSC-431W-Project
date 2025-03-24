import csv
import hashlib
import sqlite3

#helper function to sha256 hash a password
def sha256hash(password):
    hashed_pw =  hashlib.sha256(password.encode()).hexdigest()
    return hashed_pw

#set up the user table in the database by importing data from users csv file and then inserting into database tables
def u_setup():
    # Connect to (or create) the SQLite database
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Create the USERS table if it doesn't exist
    cursor.execute('CREATE TABLE IF NOT EXISTS USERS (email TEXT PRIMARY KEY NOT NULL, password TEXT NOT NULL)')

    # Read from CSV and insert rows
    with open('CSV Files/Users.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) #skip the first row that contains column headers
        for row in reader:
            email = row[0]
            hashed_password = sha256hash(row[1]) #hash the password which is the second element of each row
            cursor.execute('INSERT INTO USERS VALUES (?, ?)', (email, hashed_password))# insert into the USERS table

    # Commit the transaction and close the connection
    connection.commit()
    connection.close()

u_setup()