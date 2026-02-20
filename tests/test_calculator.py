from src.calculator import add, subtract, multiply, divide, power


class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5


class TestSubtract:
    def test_positive_numbers(self):
        assert subtract(5, 3) == 2


class TestMultiply:
    def test_positive_numbers(self):
        assert multiply(3, 4) == 12


class TestDivide:
    def test_even_division(self):
        assert divide(10, 2) == 5.0


class TestPower:
    def test_square(self):
        assert power(2, 3) == 8
