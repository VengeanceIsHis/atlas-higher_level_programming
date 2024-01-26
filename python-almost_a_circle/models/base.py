#!/usr/bin/python3
"""New module for class Base"""


class Base:
    """New class that creats the foundation for the Project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializing new instance with id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
