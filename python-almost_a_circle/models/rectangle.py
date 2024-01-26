#!/usr/bin/python3
"""Module for rectangle as a subclass to Base"""
from base.py import Base

class Rectangle(Base):
    """initializing new instance of Rectangle"""


    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing a new rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """returns the width"""
        return self.__width
    
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

    @height.setter
    def height(self, value):
        """sets the height"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__height = value

    @property
    def x(self):
        """returns location x"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """sets the location x"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__height = value

    @property
    def y(self):
        """returns the location variable y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the location y"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__y = value
