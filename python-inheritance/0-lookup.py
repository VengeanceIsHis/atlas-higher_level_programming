#!/usr/bin/python3
"""Module for new function"""


def lookup(obj):
    """New functino that rereturn (dir(obj))turns all atrributes"""
    all_attributes = lookup(obj)
    filtered_attributes = [attr for attr in all_attributes if not (attr.startswith("__") and attr.endswith("__"))]
    return filtered_attributes