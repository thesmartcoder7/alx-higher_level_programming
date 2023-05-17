#!/usr/bin/python3


def complex_delete(a_dict, val):
    if not val or val is None:
        return a_dict

    for key in a_dict:
        if a_dict[key] == val:
            del a_dict[key]
            break

    return a_dict
