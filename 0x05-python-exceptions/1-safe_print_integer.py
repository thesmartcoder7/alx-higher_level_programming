#!/usr/bin/python3


def safe_print_integer(value):
    """
        Print integers
    """
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
    except TypeError as error:
        print(error)
        return False
