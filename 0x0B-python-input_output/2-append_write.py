#!/usr/bin/python3
"""
append file and print it
"""


def append_write(filename="", text=""):
    """
    append file and print it
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return(f.write(text))
