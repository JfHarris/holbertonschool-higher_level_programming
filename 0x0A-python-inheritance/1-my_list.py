#!/usr/bin/python3
"""
inherits from list
"""


class MyList(list):
    """
    inherits from list, prints sorted list
    """
    def print_sorted(self):
        print(sorted(self))
