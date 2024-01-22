#!/usr/bin/python3
"""New module for sublass Rectangle from Geometry"""
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        if integer_validator(width) == True:
            self.__width = width
        if integer_validator(height) == True:
            self.__height = height
