#!/usr/bin/python3

'''add_item module'''
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args = sys.argv[1:]
old_list = load_from_json_file('add_item.json')
new_list = old_list + args
save_to_json_file(new_list, 'add_item.json')
