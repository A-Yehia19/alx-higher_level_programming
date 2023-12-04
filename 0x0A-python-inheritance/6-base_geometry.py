#!/usr/bin/python3

"""Module that defines a class BaseGeometry"""


class BaseGeometry():
    """Class that defines a BaseGeometry object
    Attributes:
        No Attributes for now.

    Methods:
        area(self): Raises an Exception with the message area() is not
        implemented

    Raises:
        Exception: area() is not implemented
    """
    def area(self):
        """Method that raises an Exception
        
        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")
