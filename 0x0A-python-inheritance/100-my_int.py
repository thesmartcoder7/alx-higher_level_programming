#!/usr/bin/python3
"""
Contain the class MyInt
"""


class MyInt(int):
    """opposite integers"""
    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """reverse the == operator"""
        return int(self) != other

    def __ne__(self, other):
        """reverse the != operator"""
        return int(self) == int(other)
