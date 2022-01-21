#!/usr/bin/python3
"""
append file and print number of chars
"""


def append_write(filename="", text=""):
    """
    append file and print number of chars
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return(f.write(text))
