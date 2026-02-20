from src.calculator import subtract, divide


class TestSubtract:
    def test_positive_numbers(self):
        assert subtract(5, 3) == 2


class TestDivide:
    def test_even_division(self):
        assert divide(10, 2) == 5.0
