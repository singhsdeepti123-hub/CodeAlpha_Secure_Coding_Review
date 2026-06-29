import sqlite3

def get_user_data(username):
    # INSECURE: Directly concatenating user input into SQL query (SQL Injection Vulnerability)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    
    return cursor.fetchall()
