def connect_to_database():
    username = "admin"
    password = "secret123"  # Hardcoded password
    db_url = "mysql://localhost:3306/mydb"
    # Simulate database connection
    return f"Connected with {username}:{password} to {db_url}"