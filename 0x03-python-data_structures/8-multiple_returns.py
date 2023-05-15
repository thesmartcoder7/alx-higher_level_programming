#!/usr/bin/python3


def multiple_returns(s):
    """
        This function returns a tuple with the length
        of a string and its first character
    """
    return (len(s), None) if s == '' else (len(s), s[0])
