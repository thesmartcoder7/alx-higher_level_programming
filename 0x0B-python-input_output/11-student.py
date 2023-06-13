#!/usr/bin/python3
"""Contains the clas "Student"""


class Student:
    """ a Class Representation of a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            returns a dictionary representation of a class instance
            with specified attributes
        """
        if not attrs:
            return self.__dict__
        new_dict = {}
        for att in attrs:
            try:
                new_dict[att] = self.__dict__[att]
            except KeyError:
                pass
        return new_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except KeyError:
                pass
