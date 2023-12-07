#!/usr/bin/python3

'''save_to_json_file module'''


def save_to_json_file(my_obj, filename):
    '''Writes an Object to a text file, using a JSON representation'''
    import json

    with open(file=filename, mode='w', encoding='utf-8') as f:
        json.dump(obj=my_obj, fp=f)
