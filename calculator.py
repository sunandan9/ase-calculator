"""
calculator.py
A simple calculator module providing basic arithmetic operations.
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """
    Return the quotient of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(base, exponent):
    """Return base raised to the power of exponent."""
    return base ** exponent


def modulo(a, b):
    """
    Return the remainder of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot perform modulo with zero divisor.")
    return a % b
