#!/usr/bin/python3
"""
reads file
"""


def read_file(filename=""):
    """
    read file
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
