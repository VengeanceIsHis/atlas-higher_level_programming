#!/usr/bin/python3
"""Module that creats a subclass to list"""

class MyList (list):
    """New class for printing sorted list"""
    def print_sorted(self):
    """Sorted print of the current instance"""
    print(sorted(self))