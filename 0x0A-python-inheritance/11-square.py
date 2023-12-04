#!/usr/bin/python3

"""Module that defines a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that defines a Square object

    Attributes:
        size (int): size of the Square object

    Methods:
        __init__(self, size): initializes a Square object
        area(self): returns the area of a Square object
        print(self): prints the Square description
        __str__(self): returns a string representation of a Square object

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less or equal to zero
    """
    def __init__(self, size):
        """Initializes a Square object

        Args:
            size (int): size of the Square object

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less or equal to zero
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of a Square object

        Args:
            None

        Returns:
            (int) Area of the Square object

        Raises:
            None
        """
        return self.__size ** 2

    def print(self):
        """Prints the Square description: [Square] <width>/<height>

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        print("[Square] {}/{}".format(self.__size, self.__size))

    def __str__(self):
        """Returns a string representation of a Square object

        Args:
            None

        Returns:
            (str) String representation of a Square object

        Raises:
            None
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
