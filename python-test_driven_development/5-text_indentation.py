#!/usr/bin/python3
"""Module for Text indention"""


def text_indentation(text):
    """Text indentation problem"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        count = 0
        for char in text:
            if char == '.' or char == '?' or char ==':':
                print(f"{char}", end="")
                print("\n")
            if not char == '\0':
                print(f"{char}", end="")
