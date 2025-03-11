# Rule S116 Functions should not have too many parameters
import re
import datetime
import logging
from typing import Optional

# Set up basic logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def handle_user_data(
    name: str,
    age: int,
    email: str,
    phone: str,
    address: str,
    city: str,
    country: str,
    postal_code: str,
    is_active: bool,
    last_login: Optional[datetime.datetime],
    membership_level: str,
    registration_date: datetime.date
) -> bool:
    """
    Process user data with extensive validation, logging, and status checks.
    
    Args:
        name: User's full name
        age: User's age
        email: User's email address
        phone: User's phone number
        address: User's street address
        city: User's city
        country: User's country
        postal_code: User's postal code
        is_active: User's account status
        last_login: Last login timestamp (optional)
        membership_level: User's membership tier (e.g., "Basic", "Premium")
        registration_date: Date of user registration
    
    Returns:
        bool: True if processing succeeds, False otherwise
    """
    try:
        # Basic user info logging
        logger.info(f"Processing user: {name}")
        user_status = "Active" if is_active else "Inactive"
        logger.info(f"User status: {user_status}")

        # Age validation and categorization
        if not isinstance(age, int) or age < 0:
            logger.error(f"Invalid age provided: {age}")
            return False
        if age < 18:
            logger.info("User is a minor")
            age_category = "Minor"
        elif age < 65:
            logger.info("User is an adult")
            age_category = "Adult"
        else:
            logger.info("User is a senior")
            age_category = "Senior"

        # Email validation
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_pattern, email):
            logger.warning(f"Invalid email format: {email}")
            return False
        logger.info(f"Email: {email}")
        if email.endswith("@example.com"):
            logger.info("Using example domain - test account detected")

        # Phone number validation
        phone_pattern = r"^\+\d{1,3}\d{6,14}$"
        if not re.match(phone_pattern, phone):
            logger.warning(f"Invalid phone format: {phone}")
            return False
        logger.info(f"Phone: {phone}")
        if phone.startswith("+1"):
            logger.info("US phone number detected")
        elif phone.startswith("+44"):
            logger.info("UK phone number detected")

        # Address formatting and logging
        full_address = f"{address}, {city}, {country} - {postal_code}"
        logger.info(f"Full address: {full_address}")
        if len(postal_code) < 5:
            logger.warning(f"Postal code seems too short: {postal_code}")

        # Last login processing
        if last_login:
            if not isinstance(last_login, datetime.datetime):
                logger.error(f"Invalid last_login type: {type(last_login)}")
                return False
            days_since_login = (datetime.datetime.now() - last_login).days
            logger.info(f"Last login: {last_login} ({days_since_login} days ago)")
            if days_since_login > 90:
                logger.warning("User inactive for over 90 days")

        # Membership level processing
        valid_levels = {"Basic", "Premium", "Elite"}
        if membership_level not in valid_levels:
            logger.error(f"Invalid membership level: {membership_level}")
            return False
        logger.info(f"Membership level: {membership_level}")
        if membership_level == "Premium":
            logger.info("User eligible for premium features")

        # Registration date processing
        if not isinstance(registration_date, datetime.date):
            logger.error(f"Invalid registration_date type: {type(registration_date)}")
            return False
        tenure_days = (datetime.date.today() - registration_date).days
        logger.info(f"Registered on: {registration_date} ({tenure_days} days ago)")
        if tenure_days > 365:
            logger.info("Long-term user detected")

        # Simulate additional processing
        user_summary = {
            "name": name,
            "age_category": age_category,
            "status": user_status,
            "membership": membership_level,
            "tenure_days": tenure_days
        }
        logger.info(f"User summary: {user_summary}")

        return True

    except Exception as e:
        logger.error(f"Error processing user data: {str(e)}")
        return False

# Usage example
if __name__ == "__main__":
    user_data = {
        "name": "John Doe",
        "age": 25,
        "email": "john.doe@example.com",
        "phone": "+12025550123",
        "address": "123 Elm St",
        "city": "Springfield",
        "country": "USA",
        "postal_code": "62701",
        "is_active": True,
        "last_login": datetime.datetime.now() - datetime.timedelta(days=10),
        "membership_level": "Premium",
        "registration_date": datetime.date(2022, 1, 15)
    }
    result = handle_user_data(**user_data)
    print(f"Processing result: {result}")