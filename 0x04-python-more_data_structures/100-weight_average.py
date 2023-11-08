#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    ans = 0
    quotient = 0
    for item in my_list:
        ans += item[0] * item[1]
        quotient += item[1]

    return ans / quotient
