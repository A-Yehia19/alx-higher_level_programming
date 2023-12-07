#!/usr/bin/python3

'''add_item module'''
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(args):
    '''Adds all arguments to a Python list, and then save them to a file'''
    old_list = load_from_json_file('add_item.json')
    new_list = old_list + args
    save_to_json_file(new_list, 'add_item.json')


if __name__ == '__main__':
    add_item(sys.argv[1:])
