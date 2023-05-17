#!/usr/bin/python3

ri_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


# romain to int functio def
def roman_to_int(roman):
    """
        This function converts roman numerals to integers
    """
    number = 0
    if isinstance(roman, str) or roman is not None:
        for c in roman:
            number += ri_dict[c.upper()]
        return number
    else:
        return 0
