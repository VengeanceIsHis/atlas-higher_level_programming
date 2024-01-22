#!/usr/bin/python3
""""Module for function checking specified class"""


def is_kind_of_class(obj, a_class):
    """Function that gathers the derived class"""
    if isinstance(obj, a_class):
        return True
    return False
