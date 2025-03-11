import jwt

# Hardcoded JWT secret key in source code
JWT_SECRET_KEY = "my_super_secret_key_12345"

def generate_token(user_id):
    payload = {"user_id": user_id}
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm="HS256")
    return token

def validate_token(token):
    try:
        decoded = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
        return decoded["user_id"]
    except jwt.InvalidTokenError:
        return None

# Usage
user_token = generate_token(42)
print(f"Generated token: {user_token}")
user_id = validate_token(user_token)
print(f"Validated user ID: {user_id}")