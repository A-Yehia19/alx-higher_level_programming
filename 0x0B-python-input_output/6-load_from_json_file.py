#!/usr/bin/python3

'''load_from_json_file module'''


def load_from_json_file(filename):
    '''Creates an Object from a JSON file'''
    import json

    with open(file=filename, mode='r', encoding='utf-8') as f:
        json_text = f.read()

    return json.loads(json_text)
