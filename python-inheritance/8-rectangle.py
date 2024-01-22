#!/usr/bin/python3
"""New module for sublass Rectangle from Geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Initialized subclass of Rectangle"""

    def __init__(self, width, height):
        """initialization process"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
