#!/usr/bin/python3
"""
adds all arguments to a Python list, and then save them to a file
"""

import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

size = len(sys.argv)
with open("add_item.json", 'a+') as f:
    f.seek(0)
    read_data = f.read()
    if read_data == "":
        json.dump([], f)

new = load_from_json_file("add_item.json")
for x in range(1,size):
    new.append(sys.argv[1])

save_to_json_file(new, "add_item.json")
