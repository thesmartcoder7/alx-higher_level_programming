#!/usr/bin/env python3


def no_c(my_string):
    new_string = []
    for char in my_string:
        if not char.lower() == 'c':
            new_string.append(char)

    return ''.join(new_string)
