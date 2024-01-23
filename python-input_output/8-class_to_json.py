#!/usr/bin/python3
"""Module for changing an instance of a class to json"""


def class_to_json(obj):
    """Function that returns the dictionary description of the obj passed"""
    return obj.__dict__
