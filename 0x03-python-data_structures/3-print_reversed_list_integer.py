#!/usr/bin/python3

# first variation that is weirdly checker negative
# def print_reversed_list_integer(my_list=[]):
#     for item in reversed(my_list):
#         print("{:d}".format(item))

def print_reversed_list_integer(my_list=[]):
    for i in reversed(range(len(my_list))):
        print("{:d}".format(my_list[i]))
