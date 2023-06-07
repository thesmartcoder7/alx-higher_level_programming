#!/usr/bin/python3
"""
    This module performs the addition operation between two numbers,
    these numbers can be integers or floats.
"""


def convert_to_int(num):
    """
        Convert a float number to a integer number

        Arguments:
            num (:obj:`int, float`): The number to be converted.

        Returns:
            int: The number casted to integer.
    """
    if type(num) is float:
        num = int(num)
        return num

    return num


def add_integer(a, b=98):
    """
        Performs the addition between two numbers.

        Arguments:
            a (:obj:`int, float`): The first number.
            b (:obj:`int, float`, optional): The second number.

        Returns:
            int: The result of the addition.
    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')

    if type(b) not in (int, float):
        raise TypeError('b must be an integer')

    a = convert_to_int(a)
    b = convert_to_int(b)
    return a + b
