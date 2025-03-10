def handle_user_data(name, age, email, phone, address, city, country, postal_code, is_active, last_login):
    print(f"Processing user: {name}")
    user_status = "Active" if is_active else "Inactive"
    print(f"User status: {user_status}")
    if age < 18:
        print("User is a minor")
    else:
        print("User is an adult")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Address: {address}, {city}, {country} - {postal_code}")
    if last_login:
        print(f"Last login: {last_login}")
    if email.endswith("@example.com"):
        print("Using example domain")
    if phone.startswith("+1"):
        print("US phone number detected")
    # Imagine 20 more lines of similar processing...
    return True