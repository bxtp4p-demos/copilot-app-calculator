import unittest
from unittest.mock import MagicMock
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(history_manager=MagicMock())

    def test_initialization(self):
        # Test default initialization
        calc_default = Calculator()
        self.assertIsNotNone(calc_default)
        # Test custom initialization
        custom_pow_func = lambda x, y: x ** y
        custom_pi_value = 3.14
        calc_custom = Calculator(pow_func=custom_pow_func, pi_value=custom_pi_value)
        self.assertEqual(calc_custom.pow_func(2, 3), 8)
        self.assertEqual(calc_custom.calculate_circle_area(1), 3.14)

    def test_add(self):
        self.assertEqual(self.calculator.add(5, 3), 8)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 5), 5)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)
        self.assertEqual(self.calculator.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 4), 12)
        self.assertEqual(self.calculator.multiply(-1, 1), -1)
        self.assertEqual(self.calculator.multiply(0, 10), 0)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertEqual(self.calculator.divide(-4, 2), -2)
        self.assertEqual(self.calculator.divide(0, 1), 0)
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(1, 0)

    def test_power(self):
        self.assertEqual(self.calculator.power(2, 3), 8)
        self.assertEqual(self.calculator.power(-1, 2), 1)
        self.assertEqual(self.calculator.power(0, 1), 0)

    def test_calculate_circle_area(self):
        self.assertAlmostEqual(self.calculator.calculate_circle_area(1), 3.141592653589793)
        with self.assertRaises(TypeError):
            self.calculator.calculate_circle_area(-1)
        self.assertAlmostEqual(self.calculator.calculate_circle_area(0), 0)

    def test_history_logging(self):
        self.calculator.add(1, 1)
        self.calculator.history_manager.add_entry.assert_called_with("add", 1, 1, result=2)

if __name__ == '__main__':
    unittest.main()