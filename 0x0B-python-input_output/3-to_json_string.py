#!/usr/bin/python3
"""
return JSON representation of obj
"""


def to_json_string(my_obj):
    """
    returns JSON representation of obj
    """
    import json

    return json.dumps(my_obj)
