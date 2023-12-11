#!/usr/bin/python3

'''Class Square module'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class

    Attributes:
        size (int): size of square
        x (int): x coordinate of square
        y (int): y coordinate of square
        id: id of square

    Methods:
        __init__(self, size, x=0, y=0, id=None)
        __str__(self)
        update(self, *args, **kwargs)
        to_dictionary(self)

    Raises:
        TypeError: if size/x/y is not an integer
        ValueError: if size is less than or equal to 0
        ValueError: if x/y is less than 0
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''Initializes square

        Args:
            size: size of square
            x: x coordinate of square
            y: y coordinate of square
            id: id of square

        Raises:
            TypeError: if size/x/y is not an integer
            ValueError: if size is less than or equal to 0
            ValueError: if x/y is less than 0
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''String representation of square'''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        '''Getter for size'''
        return self.width

    @size.setter
    def size(self, value):
        '''Setter for size'''
        super.validate("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Updates attributes

        Args:
            *args: list of arguments
            **kwargs: dictionary of arguments
        '''
        if len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''Returns dictionary representation of square'''
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
