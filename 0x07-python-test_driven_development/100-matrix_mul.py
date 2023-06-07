#!/usr/bin/python3
"""Module that contains a function to divide a matrix by a scalar"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for x in m_a:
        if type(x) is not list:
            raise TypeError("m_a must be a list of lists")
    for x in m_b:
        if type(x) is not list:
            raise TypeError("m_b must be a list of lists")
    if len(m_a) < 1:
        raise ValueError("m_a can't be empty")
    if len(m_b) < 1:
        raise ValueError("m_b can't be empty")
    ar_len = len(m_a[0])
    if ar_len < 1:
        raise ValueError("m_a can't be empty")
    br_len = len(m_b[0])
    if br_len < 1:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        if len(row) != ar_len:
            raise TypeError("each row of m_a must should be of the same size")
        for col in row:
            if type(col) is not float and type(col) is not int:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if len(row) != br_len:
            raise TypeError("each row of m_b must should be of the same size")
        for col in row:
            if type(col) is not float and type(col) is not int:
                raise TypeError("m_b should contain only integers or floats")
    if ar_len != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    res_matrix = []
    for x in range(len(m_a)):
        row = []
        for y in range(br_len):
            sum = 0
            for z in range(ar_len):
                sum += m_a[x][z] * m_b[z][y]
            row.append(sum)
        res_matrix.append(row)
    return res_matrix
