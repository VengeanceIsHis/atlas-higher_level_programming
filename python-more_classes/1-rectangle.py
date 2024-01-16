#!/usr/bin/python3
"""Represent a rectangle"""


class Rectangle:
    """Class documentation"""
    def __init__(self, width=0, height=0):
        """defines the size of rectangle"""
        self.__width = width
        self.__height = height
    @property
    def width(self):
        """gets the curent width of rectangle"""
        return self.__width
    @width.setter
    def width(self, value):
        """Redefines the width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
    @property
    def height(self):
        """gathers the height of an rectangle"""
        return self.__heigh
    @height.setter
    def height(self, value):
        """Redeines the height of an rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
    