#!/usr/bin/python3
"""Module that adds all arguments to a python list into a file"""


import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    file_data = load_from_json_file('add_item.json')
except FileNotFoundError:
    file_data = []
for arg in sys.argv[1:]:
    file_data.append(arg)
save_to_json_file(file_data, 'add_item.json')
