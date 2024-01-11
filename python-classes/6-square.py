#!/usr/bin/python3
"""Define a class square."""


class Square:
    """Class"""
    def __init__(self, size=0, position=(0, 0)):
        """New Square initialized"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Gathers the area of square"""

        return self.__size * self.__size

    def my_print(self):
        if size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                [print("#", end="") for j in range(self.__size)]
                print("")

            if self.__size == 0:
                print("")
