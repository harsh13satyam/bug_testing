from src.validator import validate_username, validate_age, validate_email


class TestValidateUsername:
    def test_valid_username(self):
        assert validate_username("john123") is True

    def test_short_username(self):
        assert validate_username("ab") is False

    def test_long_username(self):
        assert validate_username("a" * 21) is False

    def test_special_characters(self):
        assert validate_username("john@doe") is False

    def test_non_string_input(self):
        assert validate_username(12345) is False


class TestValidateAge:
    def test_valid_age(self):
        assert validate_age(25) is True

    def test_zero_age(self):
        assert validate_age(0) is True

    def test_negative_age(self):
        assert validate_age(-1) is False

    def test_too_old(self):
        assert validate_age(151) is False

    def test_non_integer(self):
        assert validate_age("twenty") is False


class TestValidateEmail:
    def test_valid_email(self):
        assert validate_email("user@example.com") is True

    def test_invalid_email_no_at(self):
        assert validate_email("userexample.com") is False

    def test_invalid_email_no_domain(self):
        assert validate_email("user@") is False

    def test_non_string_input(self):
        assert validate_email(12345) is False
