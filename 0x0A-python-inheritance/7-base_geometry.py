#!/usr/bin/python3

"""Module that defines a class BaseGeometry"""


class BaseGeometry():
    """Class that defines a BaseGeometry object
    Attributes:
        No Attributes for now.

    Methods:
        area(self): Raises an Exception with the message area() is not
        implemented
        integer_validator(self, name, value): validates value

    Raises:
        Exception: area() is not implemented
        TypeError: <name> must be an integer
        ValueError: <name> must be greater than 0
    """
    def area(self):
        """Method that raises an Exception
        
        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value is integer

        Args:
            name: name
            value: value to validate

        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
