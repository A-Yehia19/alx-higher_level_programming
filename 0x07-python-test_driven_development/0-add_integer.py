#!/usr/bin/python3

"""Module that adds 2 integers."""


def add_integer(a, b=98):
    """Function that adds 2 integers.

    Args:
        a (int): first integer.
        b (int): second integer.

    Returns:
        int: the addition of a and b.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
