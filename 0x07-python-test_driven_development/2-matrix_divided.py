#!/usr/bin/python3

def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix.

    Args:
        matrix (list): list of lists of integers or floats.
        div (int, float): number to divide the matrix by.

    Returns:
        list: list of lists of integers or floats.
    """
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if type(row) is not list or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if type(num) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
           new_row.append(round(num / div, 2))
        new_matrix.append(new_row)
    return new_matrix
