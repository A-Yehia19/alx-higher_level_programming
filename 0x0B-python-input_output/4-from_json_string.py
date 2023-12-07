#!/usr/bin/python3

'''from_json_string module'''


def from_json_string(my_str):
    '''Returns an Python data structure represented by a JSON string'''
    import json
    return json.loads(my_str)
