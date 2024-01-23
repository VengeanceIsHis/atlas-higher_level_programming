#!/usr/bin/python3
"""Module that returns an obj from a json file"""


import json


def load_from_json_file(filename):
    """Regression of a json file"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
