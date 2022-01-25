#!/usr/bin/python3
"""
adds all arguments to a Python list, and then save them to a file
"""

import json
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

name = "add_item.json"

try:
    prev_info = load_from_json_file(name)
except FileNotFoundError:
    prev_info = []

save_to_json_file(prev_info + argv[1:], name)
