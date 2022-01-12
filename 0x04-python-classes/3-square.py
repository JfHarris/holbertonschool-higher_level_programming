#!/usr/bin/python3

"""
Making a class named Square with a private instance attribute
Defining function within class that finds the size of square
"""

class Square:
    """
    Instantiating size and making it a private variable
    Raise type error or value error if needed
    Creating method that finds the square of number
    Using setter
    Using getter
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
