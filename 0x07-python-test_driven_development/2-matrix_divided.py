#!/usr/bin/python3
"""
    This module is in charge of dividing all the values of a matrix
    according to a divisor given by the user. 
"""


def check_for_list(value):
    """
        Check if the value is of type list

        Arguments:
            value (any): The value to verify.
        Raises:
            TypeError: If `value` isn't a list.
    """

    if type(value) is not list or len(value) == 0:
        raises_matrix_type_error()


def check_for_divisor(div):
    """
        Check if the divisor is integer, float or zero

        Arguments:
            div (any): The divisor to verify.
        Raises:
            TypeError: If `value` isn't integer or float.
            ZeroDivisionError: If `div` is equal to `0`.
    """

    if check_for_number(div) is False:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')


def check_for_number(value):
    """
        Check if the value is integer or float

        Arguments:
            value (any): The value to verify.
        Returns:
            bool: True if successful, False otherwise.
    """

    if type(value) is not int and type(value) is not float:
        return False

    """ Check for a NaN value """
    if value != value:
        return False

    return True


def check_row_size_inconsistency(e_sizes, row):
    """
        Checks the size consistency of rows in a matrix

        Arguments:
            e_sizes (:obj:`set` of :obj:`int`): Size of each row matrix.
            row (list): A row with elements to divide.
        Returns:
            set: A unique consistent size between all rows.
        Raises:
            TypeError: If `e_sizes` has more than one size in its contents.
    """

    e_sizes.add(len(row))

    if len(e_sizes) > 1:
        raise TypeError('Each row of the matrix must have the same size')

    return e_sizes


def raises_matrix_type_error():
    """
        Raises a Matrix TypeError

        Raises:
            TypeError: If `matrix` list of lists of integers or floats.
    """
    raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')


def matrix_divided(matrix, div):
    """
        Divides all elements of a matrix.

        Arguments:
            matrix (:obj:`list` of :obj:`list`): The matrix to be divided.
            div (int): The divisor number.

        Returns:
            list: A new matrix with all elements divided.

        Raises:
            TypeError: If `matrix` list of lists of integers or floats or
                if `div` is not a number.
            ZeroDivisionError: If `div` is equal to `0`.
    """

    check_for_list(matrix)
    check_for_divisor(div)

    e_sizes = set()
    res_list = list()

    for elem in matrix:
        if check_for_list(elem) is False:
            raises_matrix_type_error()

        e_sizes = check_row_size_inconsistency(e_sizes, elem)
        values = []

        for value in elem:
            if check_for_number(value) is False:
                raises_matrix_type_error()

            values.append(round(value / div, 2))

        res_list.append(values)

    return res_list
