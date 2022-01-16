#!/usr/bin/python3
"""
Add numbers.
"""


def add_integer(a, b=98):
    """
    Add numbers. Raise errors if necessary
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
