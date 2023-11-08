#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    tmp = a_dictionary.copy()
    for key in tmp.keys():
        tmp[key] *=2
    return tmp
