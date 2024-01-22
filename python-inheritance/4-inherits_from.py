#!/usr/bin/python3
"""New module for returning True if obj is of a class"""


def inherits_from(obj, a_class):
    if issubclass(type(obj)) and type(obj) != a_class:
        return True
    return False