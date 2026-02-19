from src.calculator import add, subtract, multiply, divide, power


class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-2, -3) == -5

    def test_mixed_numbers(self):
        assert add(-2, 3) == 1


class TestSubtract:
    def test_positive_numbers(self):
        assert subtract(5, 3) == 2

    def test_negative_result(self):
        assert subtract(3, 5) == -2


class TestMultiply:
    def test_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_by_zero(self):
        assert multiply(5, 0) == 0

    def test_negative_numbers(self):
        assert multiply(-2, 3) == -6


class TestDivide:
    def test_even_division(self):
        assert divide(10, 2) == 5.0

    def test_decimal_result(self):
        assert divide(7, 2) == 3.5

    def test_divide_by_zero(self):
        try:
            divide(10, 0)
            assert False, "Should have raised ValueError"
        except ValueError:
            pass


class TestPower:
    def test_square(self):
        assert power(2, 3) == 8

    def test_power_of_zero(self):
        assert power(5, 0) == 1

    def test_power_of_one(self):
        assert power(7, 1) == 7
