#!/usr/bin/python3

'''Student class module'''


class Student:
    '''Student class

    Attributes:
        first_name (str): first name of student
        last_name (str): last name of student
        age (int): age of student

    Raises:
        TypeError: if first_name is not a string
        TypeError: if last_name is not a string
        TypeError: if age is not an integer
        ValueError: if age is less than 0
    '''

    def __init__(self, first_name, last_name, age):
        '''Initializes an instance
        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            age (int): age of student

        Raises:
            TypeError: if first_name is not a string
            TypeError: if last_name is not a string
            TypeError: if age is not an integer
            ValueError: if age is less than 0
        '''
        if type(first_name) is not str:
            raise TypeError('first_name must be a string')
        if type(last_name) is not str:
            raise TypeError('last_name must be a string')
        if type(age) is not int:
            raise TypeError('age must be an integer')
        if age < 0:
            raise ValueError('age must be >= 0')

        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self):
        '''Returns the dictionary representation of a Student instance'''
        return self.__dict__
