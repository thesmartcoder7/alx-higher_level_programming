#!/usr/bin/python3


def max_integer(my_list=[]):
    """
        This function finds the biggers integer
        from a given list
    """
    if len(my_list) == 0:
        return None
    else:
        max = min(my_list)
        for item in my_list:
            if item > max:
                max = item
        return max
