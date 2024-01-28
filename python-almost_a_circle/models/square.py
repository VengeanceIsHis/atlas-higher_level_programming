#!/usr/bin/python3
"""Module for Square class derived from Rectangle which is from Base"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """New initialization through Square class"""


    def __init__(self, size, x=0, y=0, id=None):
        """Initializing new square"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returning the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        return self.width
    
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value