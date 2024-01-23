#!/usr/bin/python3
"""Module of a class called Student"""


class Student:
    """This class represents adding a student into a system"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        check = False
        check = isinstance(obj, list) and all(isinstance(item, str) for item in obj)
        if not check == False:
            return self.__dict__
