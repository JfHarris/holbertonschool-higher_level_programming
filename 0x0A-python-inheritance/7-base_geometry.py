#!/usr/bin/python3
"""
7-base_geometry class BaseGeometry
with public instances area and integer_validator
"""


class BaseGeometry:
    """
    contains methods area(self and integer_validator(self, name, value
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
