#!/usr/bin/python3
"""Module for Text indention"""


def text_indentation(text):
    """Text indentation problem"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        count = 0
        while count < len(text):
            for char in text:
                if char == '.' or char == '?' or char ==':':
                    print(f"{text}", end="")
                    print("\n")
                    count += 1
                if not char == '\0':
                    print(f"{text}", end="")
                    count += 1
