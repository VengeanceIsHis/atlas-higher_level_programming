#!/usr/bin/python3
"""New module for class Base"""


class Base:
    """New class that creats the foundation for the Project"""
    __Base__nb_objects = 0
    def __init__(self, id=None):
        """initializing new instance with id"""
        if not id == None:
            self.id = id
        else:
            __Base__nb_objects += 1
            self.id = __Base__nb_objects
