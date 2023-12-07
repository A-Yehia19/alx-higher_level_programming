#!/usr/bin/python3

'''Pascal's Triangle module'''


def pascal_triangle(n):
    '''Returns a list of lists of integers representing the Pascal's triangle
    of n'''
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            # The value at triangle[i][j] is the sum of the values
            # immediately above and to the left and above and to the right.
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
