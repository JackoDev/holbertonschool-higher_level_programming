#!/usr/bin/python3
"""
Unittest for the max_integer module
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """Test for empty list"""
    def test_empty(self):
        self.assertEqual(max_integer([]), None)
    """Test for strings"""
    def test_strings(self):
        self.assertEqual(max_integer(['H', 'o', 'l', 'a']), 'o')
    """Test for same value"""
    def test_samevalue(self):
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)
    """Test for no order list"""
    def test_no_order(self):
        self.assertEqual(max_integer([9, 6, 1, 8]), 9)
    """Test for one negative"""
    def test_one_negative(self):
        self.assertEqual(max_integer([-1]), -1)
    """Test for just one number"""
    def test_one_number(self):
        self.assertEqual(max_integer([7]), 7)
    """Test for negative numbers"""
    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
    """Test for normal cases"""
    def test_nnormal_cases(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

if __name__ == '__main__':
    unittest.main()
