#!/usr/bin/python3
"""Module for Square class derived from Rectangle which is from Base"""
from models.Rectangle import Base

class Square(Rectangle):
    """New initialization through Square class"""


    def __init(self, size, x=0, y=0, id=None):
        """Initializing new square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returning the square"""
        return "[Square] ({}) {}/{} - {}".format(id, x, y, size)
