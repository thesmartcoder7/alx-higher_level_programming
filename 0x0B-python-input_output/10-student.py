#!/usr/bin/python3
"""Contains the clas "Student"""


class Student:
    """The Class Representation of a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            returns a dictionary representation of the instance
            with specified attributes
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {s: getattr(self, s) for s in attrs if hasattr(self, s)}
        return self.__dict__
