#!/usr/bin/python3


def complex_delete(a_dict, value):
    keys = []
    for x, y in a_dict.items():
        if y == value:
            keys.append(x)

    for x in keys:
        del a_dict[x]

    return a_dict
