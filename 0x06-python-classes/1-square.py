#!/usr/bin/python3

''' Square Class'''


class Square:
    ''' Define a Square.
        Attributes:
            size (int): Size of square. -> private instance attribute
    '''
    def __init__(self, size):
        ''' Initialize Square.
            Args:
                size (int): Size of square.
        '''
        self.__size = size
