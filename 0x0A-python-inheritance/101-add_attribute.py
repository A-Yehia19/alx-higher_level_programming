#!/usr/bin/python3

"""This module contains a function add_attribute"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it is possible

    Args:
        obj (object): object to add the attribute to
        name (str): name of the attribute to add
        value (any): value of the attribute to add

    Returns:
        None

    Raises:
        TypeError: if the attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
