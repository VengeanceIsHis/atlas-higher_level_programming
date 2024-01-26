#!/usr/bin/python3
"""Module for rectangle as a subclass to Base"""
Base = __import__('base.py').Base

class Rectangle(Base):
    """initializing new instance of Rectangle"""


    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """returns the width"""
        return (self.__width)
    
    @width.setter
    def width(self, value):
        """sets the width"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__width = value
    
    @property
    def height(self, value):
        """returns the height"""
        return(self.__height)
    