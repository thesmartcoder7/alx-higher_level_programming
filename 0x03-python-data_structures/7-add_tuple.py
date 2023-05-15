#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []

    if len(tuple_a) == len(tuple_b):
        for i in range(len(tuple_a)):
            new_tuple.append(tuple_a[i] + tuple_b[i])
            # print(f"debug {new_tuple} from first loop")
    else:
        while len(tuple_b) < len(tuple_a):
            tuple_b += (0,)
        for i in range(len(tuple_a)):
            new_tuple.append(tuple_a[i] + tuple_b[i])
            # print(f" debug {new_tuple} from second loop")

    return tuple(new_tuple)
