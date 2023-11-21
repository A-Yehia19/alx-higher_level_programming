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

            Raises:
                TypeError: If size is not an integer.
                ValueError: If size is less than 0.
        '''
        # Check if size is an integer using the setter
        self.size = size

    ''' Instance method: area '''
    def area(self):
        ''' Return the current square area '''
        return self.__size ** 2

    ''' Instance property: size '''
    @property
    def size(self):
        ''' Retrieve size '''
        return self.__size

    ''' Instance method: size setter '''
    @size.setter
    def size(self, value):
        ''' Set size as integer
            Args:
                value (int): Size of square.

            Raises:
                TypeError: If size is not an integer.
                ValueError: If size is less than 0.
         '''
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >=0')
        self.__size = value

    ''' Instance method: my_print '''
    def my_print(self):
        ''' Print a square of # '''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
