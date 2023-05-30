#!/usr/bin/python3

"""This class defines a square"""


class Square:
    """This class defines an empty square"""

    def __init__(self, size=0):
        """class initializer method with data"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of the size property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the size area of the square"""
        return self.__size**2
