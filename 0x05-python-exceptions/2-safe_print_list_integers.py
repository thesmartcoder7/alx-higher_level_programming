#!/usr/bin/python3


def safe_print_list_integers(arr, items):
    """
        Print certain elements of a list
    """
    try:
        printed = 0
        for i in range(items):
            if isinstance(arr[i], int):
                print('{}'.format(arr[i]), end='')
                printed += 1
        print()
        return printed
    except IndexError as error:
        print(error)
        raise
