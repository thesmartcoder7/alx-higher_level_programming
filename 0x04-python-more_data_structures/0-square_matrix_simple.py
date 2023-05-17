#!/usr/bin/python3


def square_matrix_simple(matrix):
    new_row = []
    new_matrix = []
    for row in matrix:
        new_row = [num ** 2 for num in row]
        new_matrix.append(new_row)
        new_row = []

    return new_matrix
