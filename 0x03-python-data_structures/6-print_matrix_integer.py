#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    counter = 0
    for row in matrix:
        for num in row:
            print('{:d}'.format(num), end='')
            counter += 1
            if num == row[-1]:
                print()
            else:
                print(' ', end='')

    if counter == 0:
        print()
