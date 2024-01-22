#!/usr/bin/python3
"""New module for returning True if obj is of a class"""


def inherits_from(obj, a_class):
    """If is a subclass return True"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
