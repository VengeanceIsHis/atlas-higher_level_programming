#!/usr/bin/python3
"""Module for Text indention"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        for char in text:
            if char == '.' or char == '?' or char ==':':
                print(f"{text}", end="")
                print("\n")
            print(f"{text}", end="")
