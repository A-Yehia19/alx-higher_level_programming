#!/usr/bin/python3

''' Empty Rectangle Class'''


class Rectangle:
    ''' Define a Rectangle.
        Attributes:
            width (int): width of rectangle. -> private instance attribute
            height (int): height of rectangle. -> private instance attribute
    '''

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        ''' Print rectangle using #.'''
        if self.__width == 0 or self.__height == 0:
            return ""
        return ((str(self.print_symbol)*self.__width + "\n")*self.__height
                )[:-1]

    def __repr__(self):
        ''' Return string representation of rectangle.'''
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        ''' Print message when rectangle is deleted.'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' Return the biggest rectangle based on the area.
            Args:
                rect_1 (Rectangle): first rectangle.
                rect_2 (Rectangle): second rectangle.

            Raises:
                TypeError: rect_1 or rect_2 are not instances of Rectangle.

            Returns:
                Rectangle: biggest rectangle.
        '''
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        ''' Return a new Rectangle instance with width == height == size.
            Args:
                size (int): size of square.

            Returns:
                Rectangle: new rectangle.
        '''
        return cls(size, size)
