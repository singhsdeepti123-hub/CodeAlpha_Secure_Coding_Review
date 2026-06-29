import sqlite3

def get_user_data_secure(username):
    # SECURE: Using parameterized queries (Prepared Statements) to prevent SQL Injection
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    
    return cursor.fetchall()
