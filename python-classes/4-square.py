#!/usr/bin/python3
"""New Class"""


class Square:
    """Class"""
    def __init__(self, size=0):
        """New Square initialized"""
        self.__size = size
    @property
    def size(self):
       """gets current size of the square"""
        return self.__size
    @size_setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        def area(self):
        return (self.__size * self.__size)