#!/usr/bin/python3
"""New module for printing squares"""


def print_square(size):
    """Square function"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size == 0:
        print("", end="")
    else:
        for row in range(size):
            for i in range(size):
                print("#", end="")
            print("")
