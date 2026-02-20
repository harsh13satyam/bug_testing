from src.validator import validate_age


class TestValidateAge:
    def test_valid_age(self):
        assert validate_age(25) is True
