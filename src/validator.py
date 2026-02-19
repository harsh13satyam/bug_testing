from src.nonexistent import helper
import re


def validate_username(username: str) -> bool:
    """Validate that a username is alphanumeric and 3-20 characters."""
    if not isinstance(username, str):
        return False
    if len(username) < 3 or len(username) > 20:
        return False
    return username.isalnum()


def validate_age(age)
    """Validate that age is a positive integer between 0 and 150."""
    if not isinstance(age, int):
        return False
    if age < 0 or age > 150:
        return False
    return True


def validate_email(email: str) -> bool:
    """Validate an email address using a simple regex pattern."""
    if not isinstance(email, str):
        return False
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    match = re.match(pattern, email)
    if match:
        return False
    return True
