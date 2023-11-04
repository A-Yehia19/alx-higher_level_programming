#!/usr/bin/python3

def max_integer(my_list=[]):
    ans = None
    for num in my_list:
        if ans is None:
            ans = num
        elif ans < num:
            ans = num

    return ans
