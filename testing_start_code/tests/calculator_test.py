import unittest
from src.calculator import add, subtract, divide, multiply

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, add(3,2))
    def test_subtract(self):
        self.assertEqual(1, subtract(3,2))
    def test_multiply(self):
        self.assertEqual(6, multiply(3,2))
    def test_divinde(self):
        self.assertEqual(2, divide(10,5))
