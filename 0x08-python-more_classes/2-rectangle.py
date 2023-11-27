#!/usr/bin/python3

''' Empty Rectangle Class'''


class Rectangle:
    ''' Define a Rectangle.
        Attributes:
            width (int): width of rectangle. -> private instance attribute
            height (int): height of rectangle. -> private instance attribute
    '''
    def __init__(self, width=0, height=0):
        ''' Initialize Rectangle.
            Args:
                width (int): width of rectangle.
                height (int): height of rectangle.

            Raises:
                TypeError: width or height are not integers.
                ValueError: width or height are less than zero.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter
        Args:
            value (int): width of rectangle.

        Raises:
            TypeError: width is not an integer.
            ValueError: width is less than zero.
        '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        '''getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter
        Args:
            value (int): height of rectangle.

        Raises:
            TypeError: height is not an integer.
            ValueError: height is less than zero.
        '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    def area(self):
        ''' Return area of rectangle.'''
        return self.__width * self.__height

    def perimeter(self):
        ''' Return perimeter of rectangle.'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height)*2
