#!/usr/bin/python3

"""Module that prints a square with the character #."""


def print_square(size):
    """Function that prints a square with the character #.

    Args:
        size (int): size of the square.

    Raises:
        TypeError: If size is not an int or float.
        TypeError: If size is a float and is less than 0.
        TypeError: If size is less than 0.

    Returns:
        None.
    """
    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    size = int(size)
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
