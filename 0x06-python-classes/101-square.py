#!/usr/bin/python3

''' Square Class'''


class Square:
    ''' Define a Square.
        Attributes:
            size (int): Size of square. -> private instance attribute
            position (tuple): Position of square. -> private instance attribute
    '''
    def __init__(self, size=0, position=(0, 0)):
        ''' Initialize Square.
            Args:
                size (int): Size of square.
                position (tuple): Position of square.

            Raises:
                TypeError: If size is not an integer.
                ValueError: If size is less than 0.
                TypeError: If position is not a tuple of 2 positive integers.
        '''
        # Check if size is an integer using the setter
        self.size = size
        # Check if position is a tuple of 2 positive integers using the setter
        self.position = position

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

    ''' Instance property: position '''
    @property
    def position(self):
        ''' Retrieve position '''
        return self.__position

    ''' Instance method: position setter '''
    @position.setter
    def position(self, value):
        ''' Set position as tuple of 2 positive integers
            Args:
                value (tuple): Position of square.

            Raises:
                TypeError: If position is not a tuple of 2 positive integers.
         '''
        errmsg = 'position must be a tuple of 2 positive integers'
        if type(value) is not tuple or len(value) != 2:
            raise TypeError(errmsg)
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError(errmsg)
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError(errmsg)
        self.__position = value

    ''' Instance method: my_print '''
    def my_print(self):
        ''' Print a square of # positioned by position'''
        if self.__size == 0:
            print()
        else:
            for lines in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)

    ''' Magic method: __str__ '''
    def __str__(self) -> str:
        ''' Return the string representation of the square '''
        string = ''
        if self.__size == 0:
            string += '\n'
        else:
            for lines in range(self.__position[1]):
                string += '\n'
            for i in range(self.__size):
                string += ' ' * self.__position[0]
                string += '#' * self.__size
                string += '\n'
        return string[:-1]
