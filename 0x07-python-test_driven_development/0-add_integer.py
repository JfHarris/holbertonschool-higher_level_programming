#!/usr/bin/python3
"""
Add numbers.
"""

def add_integer(a, b=98):
    """
    Add numbers. Raise errors if necessary
    """

    if ((isinstance(a, (int, float))) and isinstance (b, (int, float))):
        a = int(a)
        b = int(b)
        return a + b
    if (isinstance(a (int, float)) is False):
        raise TypeError("a must be an integer")
    if (isinstance(b, (int, float)) is False):
        raise TypeError("b must be an integer")
