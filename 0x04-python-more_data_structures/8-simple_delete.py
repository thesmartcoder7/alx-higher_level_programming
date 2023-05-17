#!/usr/bin/python3


def simple_delete(sm_dict, key):
    if key not in sm_dict.keys():
        return sm_dict
    else:
        sm_dict.pop(key)
        return sm_dict
