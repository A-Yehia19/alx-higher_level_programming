#!/usr/bin/python3

"""Module that defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that defines a Rectangle object

    Attributes:
        width (int): width of the Rectangle object
        height (int): height of the Rectangle object

    Methods:
        __init__(self, width, height): initializes a Rectangle object
        area(self): returns the area of a Rectangle object
        print(self): prints the Rectangle description
        __str__(self): returns a string representation of a Rectangle object

    Raises:
        TypeError: if width or height are not integers
        ValueError: if width or height are less or equal to zero
    """
    def __init__(self, width, height):
        """Initializes a Rectangle object

        Args:
            width (int): width of the Rectangle object
            height (int): height of the Rectangle object

        Raises:
            TypeError: if width or height are not integers
            ValueError: if width or height are less or equal to zero
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of a Rectangle object

        Args:
            None

        Returns:
            (int) Area of the Rectangle object

        Raises:
            None
        """
        return self.__width * self.__height

    def print(self):
        """Prints the Rectangle description: [Rectangle] <width>/<height>

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        print("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

    def __str__(self):
        """Returns a string representation of a Rectangle object

        Args:
            None

        Returns:
            (String) Representation of a Rectangle object

        Raises:
            None
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
