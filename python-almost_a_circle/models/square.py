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

    def update(self, *args, *kwargs):
        """Function that updates all attributes in an instance called to Square"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
