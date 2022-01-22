#!/usr/bin/python3
"""
Returns info from JSON string
"""


def from_json_string(my_str):
    """
    returns info from JSON string
    """
    import json

    return json.loads(my_str)
