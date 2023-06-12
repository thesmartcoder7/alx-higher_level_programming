#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """
    Updates attribute with value.

    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add.
        value (any): The value of att.
    Raises:
        TypeError: should adding the attribute fail.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
