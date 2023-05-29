#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
        execute a function safely
    """
    try:
        result = fct(*args)
    except IndexError:
        result = None
        sys.stderr.write("Exception: list index out of range\n")
    except ZeroDivisionError:
        result = None
        sys.stderr.write("Exception: division by zero\n")

    return result
