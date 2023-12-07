#!/usr/bin/python3

'''class_to_json module'''


def class_to_json(obj):
    '''Returns the dictionary description for JSON of an object'''
    return obj.__dict__
