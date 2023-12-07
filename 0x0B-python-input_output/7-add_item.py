#!/usr/bin/python3

'''add_item module'''
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    old_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    old_list = []

new_list = old_list + sys.argv[1:]
save_to_json_file(new_list, 'add_item.json')
