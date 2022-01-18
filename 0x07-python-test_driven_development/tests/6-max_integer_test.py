#!/usr/bin/python3
"""creating a Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    """
    Unittest for max_integer
    """

    def test_incorrect(self):
        """
        testing for passing args of several incorrect types
        """
        self.assertRaises(Exception, max_integer, [3.14, 46, "oops"])


    def test_correct(self):
        """
        testing for successes
        """

        self.assertEqual(max_integer([7, 9, 6, 4]), 9)
        self.assertEqual(max_integer([2, 4]), 4)
        self.assertEqual(max_integer([-7, -1, 12]), 12)
        self.assertEqual(max_integer([9, 8, 7]), 9)
        self.assertEqual(max_integer([-4, -5, -6]), -4)
        self.assertEqual(max_integer([4]), 4)

    def test_empty(self):
        """
        Testing for arg = None
        """
        self.assertIsNone(max_integer())
