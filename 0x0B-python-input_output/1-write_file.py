#!/usr/bin/python3
"""
Writes to a file
"""


from statistics import mode


def write_file(filename="", text=""):
    """
    writes to text file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return(f.write(text))
