#!/usr/bin/python3
"""Module for Text indention"""


def text_indentation(text):
    """Text indentation problem"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        for char in text:
            if char == '.' or char == '?' or char ==':':
                print(char, end="")
                print("")
            if not char == '\0':
                print(char, end="")
