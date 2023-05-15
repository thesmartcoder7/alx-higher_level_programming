#!/usr/bin/python3


def divisible_by_2(arr):
    """
        This funcition finds all the multiples
        of 2
    """
    return [True if i % 2 == 0 else False for i in arr] if arr else None
