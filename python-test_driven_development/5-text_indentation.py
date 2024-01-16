#!/usr/bin/python3
"""Module for Text indention"""


def text_indentation(text):
    """Text indentation problem"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        skip_space = False
        for char in text:
            if char in ['.', '?', ':']:
                print(char)
                print("")
                skip_space = True
            elif char ==' ' and skip_space:
                continue
            elif char != '\n':
                print(char, end="")
                skip_space = False
