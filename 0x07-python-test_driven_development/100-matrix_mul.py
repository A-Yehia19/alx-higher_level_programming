#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices

    Args:
        m_a: first matrix
        m_b: second matrix

    Raises:
        TypeError: if m_a or m_b are not lists
        TypeError: if m_a or m_b are not lists of lists
        TypeError: if m_a or m_b contain elements that are not int or float
        TypeError: if m_a or m_b are empty lists or matrices
        TypeError: if m_a or m_b are not rectangular

    Returns:
        new matrix
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")

    for row in m_a:
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # create new matrix diminsion filled with 0
    new_matrix = []
    for i in range(len(m_a)):
        new_matrix.append([])
        for j in range(len(m_b[0])):
            new_matrix[i].append(0)

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                new_matrix[i][j] += m_a[i][k] * m_b[k][j]
    return new_matrix
