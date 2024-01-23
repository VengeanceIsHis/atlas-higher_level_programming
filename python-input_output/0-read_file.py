#!/usr/bin/python3
"""Opening and reading a file"""


def read_file(filename=""):
    """Function that finds the file and reads it"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
