from flask import Flask, render_template, request, flash, session
import sqlite3 as sql
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for using flash messages
host = 'http://127.0.0.1:5000/'

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login(): #login request. returns home page if valid login, flash message if invalid
    error = None
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if is_valid_login(email, password):
            # Login successful
            return render_template('home.html')
        else:
            # Login failed - flash an error message
            flash('Login attempt failed. Invalid email or password.', 'error')
            return render_template('login.html')
    
    # If GET request, just show the login page
    return render_template('login.html')

def is_valid_login(email, password): #returns true if email & password in db, false otherwise
    connection = sql.connect('database.db')
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    output = connection.execute('SELECT * FROM USERS WHERE email = ? AND password = ?', (email, hashed_password)).fetchone()
    if output:
        return True
    else:
        return False

if __name__ == "__main__":
    app.run(debug=True)