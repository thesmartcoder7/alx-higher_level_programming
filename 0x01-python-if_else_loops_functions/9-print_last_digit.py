#!/usr/bin/python3

def print_last_digit(number):
    if len(str(number)) > 1:
        print(str(number)[-1], end='')
        return str(number)[-1]
    else:
        print(str(number), end='')
        return str(number)
