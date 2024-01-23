#!/usr/bin/python3
"""New module for adding a string to the end of a file"""


def append_write(filename="", text=""):
    """Function that appends to a file or creates a new file with text added"""
    with open(filename, 'a', encoding="utf-8") as f:
        f.append_write(text)
