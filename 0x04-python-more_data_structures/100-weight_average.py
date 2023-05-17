#!/usr/bin/python3


def weight_average(a_list):
    if len(a_list) == 0 or a_list is None:
        return 0

    numerator = 0
    denomenator = 0

    for item in a_list:
        numerator += (item[0]*item[1])
        denomenator += item[1]

    return numerator/denomenator
