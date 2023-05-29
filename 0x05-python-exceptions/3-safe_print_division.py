#!/usr/bin/python3


def safe_print_division(a, b):
    """
        Print safe division
    """
    res = 0

    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print('Inside result: {}'.format(res))
        return res
