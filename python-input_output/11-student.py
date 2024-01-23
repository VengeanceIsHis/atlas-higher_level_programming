#!/usr/bin/python3
"""Module of a class called Student"""


class Student:
    """This class represents adding a student into a system"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Changes attributes to a dictionary representation"""
        if (attrs is not None and isinstance(attrs, list) and
            all(isinstance(ele, str) for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
    
    def reload_from_json(self, json):
        """Replaces attributes with key value pairs"""
        for k, v in json.items():
            setattr(self, k, v)
