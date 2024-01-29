#!/usr/bin/python3
"""New module for class Base"""

class Base:
    """New class that creates the foundation for the Project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing a new instance with id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """New function that returns the json representatino of list_dictionaries"""
        return json.dumps(list_dictionaries)
