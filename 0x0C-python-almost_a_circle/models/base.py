#!/usr/bin/python3

'''Base module'''
import json


class Base:
    '''Base class

    Attributes:
        __nb_objects (int): number of objects

    Methods:
        __init__(self, id=None)

    Raises:
        NONE
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initializes Base

        Args:
            id: id of object
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns JSON string representation of list_dictionaries

        Args:
            list_dictionaries: list of dictionaries

        Returns:
            JSON string representation of list_dictionaries
        '''
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Writes JSON string representation of list_objs to file

        Args:
            list_objs: list of objects
        '''
        with open("{}.json".format(cls.__name__), 'w') as file:
            if list_objs is None:
                file.write('[]')
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        '''Returns list of JSON string representation

        Args:
            json_string: string representing list of dictionaries

        Returns:
            list of JSON string representation
        '''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Returns instance with attributes already set

        Args:
            **dictionary: dictionary of attributes to set

        Returns:
            instance with attributes already set
        '''
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''Returns list of instances

        Args:
            NONE

        Returns:
            list of instances
        '''
        try:
            with open("{}.json".format(cls.__name__), 'r') as file:
                list_dicts = Base.from_json_string(file.read())
                list_instances = []
                for dict in list_dicts:
                    list_instances.append(cls.create(**dict))

                return list_instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Writes CSV string representation of list_objs to file

        Args:
            list_objs: list of objects
        '''
        with open("{}.csv".format(cls.__name__), 'w') as file:
            if list_objs is None:
                file.write('[]')
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @classmethod
    def load_from_file_csv(cls):
        '''Returns list of instances

        Args:
            NONE

        Returns:
            list of instances
        '''
        try:
            with open("{}.csv".format(cls.__name__), 'r') as file:
                list_dicts = cls.from_json_string(file.read())
                list_instances = []
                for dict in list_dicts:
                    list_instances.append(cls.create(**dict))

                return list_instances
        except FileNotFoundError:
            return []
