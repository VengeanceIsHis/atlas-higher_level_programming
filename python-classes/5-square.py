#!/usr/bin/python3
"""Define a class square."""


class Square:
    """Class"""
    def __init__(self, size=0):
        """New Square initialized"""
        self.__size = size

    @property
    def size(self):
        """gets current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Redefines the size of a square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
    def area(self):
        """Gathers the area of square"""
        return (self.__size * self.__size)
    def my_print(self):
        for row in area:
            for i in row:
                print("#")
                