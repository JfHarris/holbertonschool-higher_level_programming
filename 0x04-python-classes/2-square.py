#!/usr/bin/python3

"""
Making class named square with private instance attribute
Definie function to find size
"""

class Square:

    """
    Instantiating method to check if size is an greater than zero
    Creating method to return size
    """

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size
