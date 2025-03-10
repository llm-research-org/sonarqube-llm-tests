import sqlite3

def get_user_data(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = " + str(user_id)  # Vulnerable to injection
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result