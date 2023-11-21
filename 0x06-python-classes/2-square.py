#!/usr/bin/python3

''' Square Class'''


class Square:
    ''' Define a Square.
        Attributes:
            size (int): Size of square. -> private instance attribute
    '''
    def __init__(self, size=0):
        ''' Initialize Square.
            Args:
                size (int): Size of square.
        '''
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
