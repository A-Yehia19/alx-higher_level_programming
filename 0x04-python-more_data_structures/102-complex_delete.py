#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if value is not None or value not in a_dictionary.values():
        for key, val in list(a_dictionary.items()):
            if val == value:
                del a_dictionary[key]

    return a_dictionary
