#!/usr/bin/python3
"""
8-rectangle contains class BaseGeometry, public instance methods
area and integer_validator
SubClass Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """inherits methods from BaseGeometry
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
