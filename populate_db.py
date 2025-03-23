import pandas as pd
import sqlite3
import hashlib
import os

def hash_password(password):
    """
    Hash a password using SHA-256
    """
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def create_database():
    """
    Create the database schema for the NittanyBusiness system
    """
    print("Creating database...")
    
    # Check if database file exists and remove it (for fresh start)
    if os.path.exists('nittany_business.db'):
        os.remove('nittany_business.db')
    
    # Connect to the database
    conn = sqlite3.connect('nittany_business.db')
    cursor = conn.cursor()
    
    # Create Users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        email VARCHAR(255) PRIMARY KEY,
        password_hash VARCHAR(255) NOT NULL,
        user_type VARCHAR(50) NOT NULL
    )
    ''')
    
    conn.commit()
    print("Database schema created successfully.")
    return conn, cursor

def populate_users(cursor):
    """
    Populate the Users table with data from CSV files
    """
    print("\nPopulating database with users...")
    
    # Load data from Sellers.csv
    try:
        print("\nProcessing Sellers.csv...")
        sellers_df = pd.read_csv('Sellers.csv')
        print(f"Found {len(sellers_df)} sellers")
        
        for index, row in sellers_df.iterrows():
            # For demo purposes, creating a password based on email
            password = f"seller_{row['email']}"
            password_hash = hash_password(password)
            
            cursor.execute(
                'INSERT INTO Users (email, password_hash, user_type) VALUES (?, ?, ?)',
                (row['email'], password_hash, 'seller')
            )
            
            # Print sample data for first 2 sellers
            if index < 2:
                print(f"Added seller: {row['email']}")
                print(f"  Business: {row['business_name']}")
                print(f"  Password: {password}")
                print(f"  Hash: {password_hash[:15]}...{password_hash[-15:]}")
                print()
        
        print(f"Successfully added {len(sellers_df)} sellers")
    except Exception as e:
        print(f"Error processing Sellers.csv: {e}")
    
    # Load data from Buyers.csv
    try:
        print("\nProcessing Buyers.csv...")
        buyers_df = pd.read_csv('Buyers.csv')
        print(f"Found {len(buyers_df)} buyers")
        
        for index, row in buyers_df.iterrows():
            password = f"buyer_{row['email']}"
            password_hash = hash_password(password)
            
            cursor.execute(
                'INSERT INTO Users (email, password_hash, user_type) VALUES (?, ?, ?)',
                (row['email'], password_hash, 'buyer')
            )
            
            # Print sample data for first 2 buyers
            if index < 2:
                print(f"Added buyer: {row['email']}")
                print(f"  Business: {row['business_name']}")
                print(f"  Password: {password}")
                print(f"  Hash: {password_hash[:15]}...{password_hash[-15:]}")
                print()
        
        print(f"Successfully added {len(buyers_df)} buyers")
    except Exception as e:
        print(f"Error processing Buyers.csv: {e}")
    
    # Load data from Helpdesk.csv
    try:
        print("\nProcessing Helpdesk.csv...")
        helpdesk_df = pd.read_csv('Helpdesk.csv')
        print(f"Found {len(helpdesk_df)} helpdesk staff")
        
        for index, row in helpdesk_df.iterrows():
            password = f"helpdesk_{row['email']}"
            password_hash = hash_password(password)
            
            cursor.execute(
                'INSERT INTO Users (email, password_hash, user_type) VALUES (?, ?, ?)',
                (row['email'], password_hash, 'helpdesk')
            )
            
            # Print sample data for first 2 helpdesk staff
            if index < 2:
                print(f"Added helpdesk: {row['email']}")
                print(f"  Position: {row['Position']}")
                print(f"  Password: {password}")
                print(f"  Hash: {password_hash[:15]}...{password_hash[-15:]}")
                print()
        
        print(f"Successfully added {len(helpdesk_df)} helpdesk staff")
    except Exception as e:
        print(f"Error processing Helpdesk.csv: {e}")

def display_database_stats(conn):
    """
    Display statistics about the populated database
    """
    cursor = conn.cursor()
    
    print("\n--- DATABASE STATISTICS ---")
    
    # Count total users
    cursor.execute("SELECT COUNT(*) FROM Users")
    total_users = cursor.fetchone()[0]
    print(f"Total Users: {total_users}")
    
    # Count users by type
    cursor.execute("SELECT user_type, COUNT(*) FROM Users GROUP BY user_type")
    user_counts = cursor.fetchall()
    for user_type, count in user_counts:
        print(f"{user_type.capitalize()} users: {count}")
    
    print("\n--- SAMPLE USER DATA ---")
    # Display some sample data
    cursor.execute("SELECT email, user_type FROM Users LIMIT 10")
    sample_users = cursor.fetchall()
    for email, user_type in sample_users:
        print(f"Email: {email}, Type: {user_type}")

def main():
    """
    Main function to create and populate the database
    """
    try:
        # Create database and schema
        conn, cursor = create_database()
        
        # Populate users
        populate_users(cursor)
        
        # Commit changes
        conn.commit()
        
        # Display database statistics
        display_database_stats(conn)
        
        print("\nDatabase population completed successfully!")
        print("You can now run the app.py file to start the Flask application.")
        
    except Exception as e:
        print(f"Error during database population: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    main()