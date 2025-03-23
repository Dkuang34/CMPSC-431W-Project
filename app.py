from flask import Flask, render_template, request
import sqlite3 as sql
import hashlib
import pandas as pd

app = Flask(__name__)

host = 'http://127.0.0.1:5000/'

#TODO: add popup for invalid logins showing that "login attempt failed"

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login(): #login request. returns home page if valid login, false if invalid
    email = request.form.get('email')
    password = request.form.get('password')
    if is_valid_login(email, password):
        return render_template('home.html')
    else:
        return render_template('login.html')

def is_valid_login(email, password): #returns true if email & password in db, false otherwise
    connection = sql.connect('database.db')
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    output = connection.execute('SELECT * FROM USERS WHERE email = ? AND password = ?', (email, hashed_password)).fetchone()
    if output:
        return True
    else:
        return False




"""
@app.route('/name', methods=['POST', 'GET'])
def name():
    error = None
    if request.method == 'POST':
        result = valid_name(request.form['FirstName'], request.form['LastName'])
        if result:
            return render_template('input.html', error=error, result=result)
        else:
            error = 'invalid input name'
    return render_template('input.html', error=error)


def valid_name(first_name, last_name):
    connection = sql.connect('database.db')
    connection.execute('CREATE TABLE IF NOT EXISTS users(firstname TEXT, lastname TEXT);')
    #connection.execute('INSERT INTO users (firstname, lastname) VALUES (?,?);', (first_name, last_name))
    connection.commit()
    cursor = connection.execute('SELECT * FROM users;')
    return cursor.fetchall()
"""

if __name__ == "__main__":
    app.run()


