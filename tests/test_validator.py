from src.validator import validate_username, validate_age, validate_email


class TestValidateUsername:
    def test_valid_username(self):
        assert validate_username("john123") is True


class TestValidateAge:
    def test_valid_age(self):
        assert validate_age(25) is True


class TestValidateEmail:
    def test_valid_email(self):
        assert validate_email("user@example.com") is True
