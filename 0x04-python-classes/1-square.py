#!/usr/bin/python3
"""
Making class named square with private instance attribute
"""

class Square:
    """
    instantiating variables self and size
    Raise value or type error if needed
    """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
