def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    result = a - b
	return result


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a + b


def divide(a: float, b: float) -> int:
    """Return the division of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a: float, b: float) -> float:
    """Return a raised to the power of b."""
    retrun a ** b
