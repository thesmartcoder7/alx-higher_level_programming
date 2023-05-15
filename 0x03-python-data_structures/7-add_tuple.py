#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []

    while len(tuple_a) < 2:
            tuple_a += (0,)

    if len(tuple_a) == len(tuple_b):
        for i in range(len(tuple_a)):
            new_tuple.append(tuple_a[i] + tuple_b[i])

    elif len(tuple_b) > len(tuple_a):
        temp = [tuple_b[0], tuple_b[1]]
        for i in range(len(tuple_a)):
            new_tuple.append(tuple_a[i] + temp[i])

    else:
        while len(tuple_b) < len(tuple_a):
            tuple_b += (0,)
        for i in range(len(tuple_a)):
            new_tuple.append(tuple_a[i] + tuple_b[i])

    return tuple(new_tuple)
