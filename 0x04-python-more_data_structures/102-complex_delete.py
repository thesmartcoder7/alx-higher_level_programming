#!/usr/bin/python3


def complex_delete(a_dict, val):
    if not val or val is None:
        return a_dict

    for key, value in dict(a_dict).items():
        if value == val:
            del a_dict[key]
            break

    return a_dict
