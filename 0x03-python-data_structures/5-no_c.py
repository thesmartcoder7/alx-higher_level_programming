#!/usr/bin/env python3


def no_c(my_string):
    """
    remove any 'c' or 'C' character from a string
    """
    new_string = []
    for char in my_string:
        if not char.lower() == 'c':
            new_string.append(char)

    return ''.join(new_string)
