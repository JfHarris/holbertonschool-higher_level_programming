#!/usr/bin/python3
"""
Print a square made of #
"""


def print_square(size):
    """
    Raise errors if needed
    """
    if isinstance(size, bool):
        raise TypeError("size must be an integer")
    if not isinstance(size, (int, float)) and not isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for x in range(0, int(size)):
        print("#" * (size))
