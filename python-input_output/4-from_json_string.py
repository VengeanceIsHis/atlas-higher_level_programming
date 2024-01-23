#!/usr/bin/python3
"""Module which utilizes json import to manipulate strings"""


import json


def from_json_string(my_str):
    """This function returns an object from json"""
    return json.loads(my_str)
