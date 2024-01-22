#!/usr/bin/python3
"""New module for sublass Rectangle from Geometry."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """New subclass Square from Rectangle class"""
    def __init__(self, size):
        """initializing a Square"""
        self.integer_validator("size", int)
        if size > 0:
            self.__size = size
    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size
