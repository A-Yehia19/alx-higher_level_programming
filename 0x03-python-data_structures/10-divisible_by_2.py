#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    final = []
    for num in my_list:
        final.append(num % 2 == 0)

    return final
