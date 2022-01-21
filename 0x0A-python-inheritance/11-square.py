#!/usr/bin/python3
"""
10-square contains class BaseGeometry with public instance methods
area and integer_validator
Subclass Rectangle with attributes
width and height
Subclass Square with private attribute
size"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    inherits from Rectangle which inherits from BaseGeometry
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "{:s} {:d}/{:d}".format(self.__class__.__name__, self.__size, self.__size)
