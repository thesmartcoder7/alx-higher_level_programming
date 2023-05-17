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
    if not isinstance(roman, str) or roman is None:
        return 0

    number = 0
    for i in range(len(roman)):
        if ri_dict[roman[i]] == 0:
            return 0
        if (i != (len(roman) - 1) and
                ri_dict[roman[i]] < ri_dict[roman[i + 1]]):
            number += ri_dict[roman[i]] * -1

        else:
            number += ri_dict[roman[i]]
    return number
