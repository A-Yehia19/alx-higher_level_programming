#!/usr/bin/python3

'''Class Rectangle module'''
from models.base import Base


class Rectangle(Base):
    '''Class Rectangle inherits from Base

    Attributes:
        width (int): width of rectangle
        height (int): height of rectangle
        x (int): x coordinate of rectangle
        y (int): y coordinate of rectangle
        id: id of rectangle

    Methods:
        __init__(self, width, height, x=0, y=0, id=None)
        validate(self, name, value)
        area(self)
        display(self)
        __str__(self)
        update(self, *args, **kwargs)
        to_dictionary(self)

    Raises:
        TypeError: if width/height/x/y is not an integer
        ValueError: if width/height is less than or equal to 0
        ValueError: if x/y is less than 0
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initializes rectangle

        Args:
            width: width of rectangle
            height: height of rectangle
            x: x coordinate of rectangle
            y: y coordinate of rectangle
            id: id of rectangle

        Raises:
            TypeError: if width/height/x/y is not an integer
            ValueError: if width/height is less than or equal to 0
            ValueError: if x/y is less than 0
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Getter for width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for width'''
        self.validate("width", value)
        self.__width = value

    @property
    def height(self):
        '''Getter for height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for height'''
        self.validate("height", value)
        self.__height = value

    @property
    def x(self):
        '''Getter for x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter for x'''
        self.validate("x", value)
        self.__x = value

    @property
    def y(self):
        '''Getter for y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Setter for y'''
        self.validate("y", value)
        self.__y = value

    def validate(self, name, value):
        '''Validates values

        Args:
            name: name of value
            value: value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0 for width/height
            ValueError: if value is less than 0 for x/y
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if name in ["width", "height"] and value <= 0:
            raise ValueError("{} must be > 0".format(name))

        if name in ["x", "y"] and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        '''Returns area of rectangle

        Args:
            NONE

        Returns:
            Area of rectangle
        '''
        return self.width * self.height

    def display(self):
        '''Prints rectangle
        Args:
            NONE

        Returns:
            NONE
        '''
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        '''Returns string representation of rectangle'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        '''Updates attributes

        Args:
            *args: list of arguments
            **kwargs: dictionary of arguments
        '''
        if len(args) > 0:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''Returns dictionary representation of rectangle'''
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
