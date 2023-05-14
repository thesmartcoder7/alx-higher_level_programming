#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return list(my_list).copy()
    else:
        return my_list[:idx] + [element] + my_list[idx+1:]
