#!/usr/bin/python3
"""Prints the name given in function"""


def say_my_name(first_name, last_name=""):
    """Printing name"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
