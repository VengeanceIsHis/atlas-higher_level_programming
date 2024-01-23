#!/usr/bin/python3
"""Module that adds all arguments to a python list into a file"""


import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
for arg in sys.argv:
    json_list = save_to_json_file(arg, add_item.json)
load_from_json_file(add_item.json)
