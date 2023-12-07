#!/usr/bin/python3

'''save_to_json_file module'''


def save_to_json_file(my_obj, filename):
    '''Writes an Object to a text file, using a JSON representation'''
    import json

    json_text = json.dumps(my_obj)
    with open(file=filename, mode='w', encoding='utf-8') as f:
        f.write(json_text)
