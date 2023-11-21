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
        if type(value) is not int and type(value) is not float:
            raise TypeError('size must be a number')
        elif value < 0:
            raise ValueError('size must be >=0')
        self.__size = value

    ''' Magic operator: __eq__ '''
    def __eq__(self, __value: object) -> bool:
        ''' check equality between area of 2 squares'''
        return self.area() == __value.area()

    ''' Magic operator: __ne__ '''
    def __ne__(self, __value: object) -> bool:
        ''' check inequality between area of 2 squares'''
        return self.area() != __value.area()

    ''' Magic operator: __lt__ '''
    def __lt__(self, __value: object) -> bool:
        ''' check if area of this node is
            less than area of other square
        '''
        return self.area() < __value.area()

    ''' Magic operator: __le__ '''
    def __le__(self, __value: object) -> bool:
        ''' check if area of this node is
            less than or equal to area of other square
        '''
        return self.area() <= __value.area()

    ''' Magic operator: __gt__ '''
    def __gt__(self, __value: object) -> bool:
        ''' check if area of this node is
            greater than area of other square
        '''
        return self.area() > __value.area()

    ''' Magic operator: __ge__ '''
    def __ge__(self, __value: object) -> bool:
        ''' check if area of this node is
            greater than or equal to area of other square
        '''
        return self.area() >= __value.area()
