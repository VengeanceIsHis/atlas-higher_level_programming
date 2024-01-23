#!/usr/bin/python3
"""This module utilizes json to manipulate a string into a file"""

import json


def save_to_json_file(my_obj, filename):
    """This function sends an obj to a file in json format"""
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, filename)
