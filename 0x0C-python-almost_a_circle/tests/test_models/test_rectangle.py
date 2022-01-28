#!/usr/bin/python3
"""
UnitTest for Rectangle class
"""

import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangleclass(unittest.TestCase):
    """
    unittest for Rectangle class
    """
    # correct
    # all args incorrect
    # no args
    def setUp(self):
        self.inst = Rectangle(1, 2, 3, 4, 5)

    def test_width(self):
        """
        test rectangle height
        """
        self.assertEqual(self.inst.width, 1)

    def test_width(self):
        """
        test rectangle width
        """
        self.assertEqual(self.inst.height, 2)

    def test_x(self):
        """
        text x
        """
        self.assertEqual(self.inst.x, 3)

    def test_y(self):
        """
        test y
        """
        self.assertEqual(self.inst.y, 4)
