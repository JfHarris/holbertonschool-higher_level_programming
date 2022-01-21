#!/usr/bin/python3
"""
4-inherits_from is True if obj is instance if inherits from class
or subclass"""


def inherits_from(obj, a_class):
    """
    True if obj is instance if inherits from class
    or subclass
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
