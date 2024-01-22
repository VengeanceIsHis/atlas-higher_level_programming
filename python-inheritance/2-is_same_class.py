#!/usr/bin/python3
"""New module for testing objects"""


def is_same_class(obj, a_class):
    """Learning how to do test functions"""
    if obj == "True" or obj == "False":
        return False
    if not isinstance(obj, a_class):
        return False
    return True
