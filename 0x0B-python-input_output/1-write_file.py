#!/usr/bin/python3

'''write_file module'''


def write_file(filename="", text=""):
    '''Writes a string to a text file (UTF8) and returns the number'''
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
