#!/usr/bin/python3
"""Module for writing a string to a text file"""


def write_file(filename="", text=""):
    """Function that adds a string called text into file name"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
