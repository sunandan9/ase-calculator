"""
test_calculator.py
Unit tests for the calculator module.
"""
import unittest
from calculator import add, subtract, multiply, divide, power, modulo


class TestAdd(unittest.TestCase):
    """Tests for the add() function."""

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -4), -5)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_add_floats(self):
        self.assertAlmostEqual(add(1.1, 2.2), 3.3, places=5)


class TestSubtract(unittest.TestCase):
    """Tests for the subtract() function."""

    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_subtract_resulting_negative(self):
        self.assertEqual(subtract(3, 7), -4)

    def test_subtract_zero(self):
        self.assertEqual(subtract(5, 0), 5)


class TestMultiply(unittest.TestCase):
    """Tests for the multiply() function."""

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(5, 0), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-3, -4), 12)

    def test_multiply_mixed_sign(self):
        self.assertEqual(multiply(-2, 5), -10)


class TestDivide(unittest.TestCase):
    """Tests for the divide() function."""

    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5.0)

    def test_divide_resulting_float(self):
        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError) as ctx:
            divide(5, 0)
        self.assertIn("zero", str(ctx.exception).lower())

    def test_divide_negative_dividend(self):
        self.assertEqual(divide(-9, 3), -3.0)


class TestPower(unittest.TestCase):
    """Tests for the power() function."""

    def test_power_positive_exponent(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_zero_exponent(self):
        self.assertEqual(power(5, 0), 1)

    def test_power_negative_exponent(self):
        self.assertAlmostEqual(power(2, -1), 0.5)


class TestModulo(unittest.TestCase):
    """Tests for the modulo() function."""

    def test_modulo_basic(self):
        self.assertEqual(modulo(10, 3), 1)

    def test_modulo_no_remainder(self):
        self.assertEqual(modulo(9, 3), 0)

    def test_modulo_by_zero_raises(self):
        with self.assertRaises(ValueError) as ctx:
            modulo(5, 0)
        self.assertIn("zero", str(ctx.exception).lower())


if __name__ == "__main__":
    unittest.main()
