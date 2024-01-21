#!/usr/bin/python3
"""Module for new function"""
def lookup(obj):
    """New functino that returns all atrributes"""
    attributes =[]
    for key in dir(obj):
        attributes.append(key)
    return attributes
