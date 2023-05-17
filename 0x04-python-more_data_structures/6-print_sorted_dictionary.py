#!/usr/bin/python3


def print_sorted_dictionary(dict):
    for item in sorted(dict):
        print(f"{item}: {dict[item]}")
