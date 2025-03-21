import pandas as pd
import hashlib
import sqlite3
import sys

# Define file names
CSV_FILE = 'Users.csv'
DB_FILE = 'database.db'


def hash_password(password):
    sha_signature = hashlib.sha256(password.encode()).hexdigest()
    return sha_signature
print(hash_password("<PASSWORD>"))

with open(CSV_FILE) as csvfile:
    reader = csv.reader(csvfile)






