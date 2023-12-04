#!/usr/bin/python3

"""Module that defines a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that defines a Square object"""
    def __init__(self, size):
        """Initializes a Square object"""
        pass

    def area(self):
        """Returns the area of a Square object"""
        pass

    def print(self):
        """Prints the Square description: [Square] <width>/<height>"""
        pass

    def __str__(self):
        """Returns a string representation of a Square object"""
        pass
