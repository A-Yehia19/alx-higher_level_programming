#!/usr/bin/python3

def search_replace(my_list, search, replace):
    tmp = []
    for num in my_list:
        if num == search:
            tmp.append(replace)
        else:
            tmp.append(search)

    return tmp
