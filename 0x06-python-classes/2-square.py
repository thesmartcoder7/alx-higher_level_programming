#!/usr/bin/python3

"""This class defines a square"""


class Square:
    """This class defines an empty square"""

    def __init__(self, size):
        """class initializer method with data"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
