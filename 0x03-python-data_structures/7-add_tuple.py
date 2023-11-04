#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # put 2 zeros at the end (redudndant if len >=2)
    # in case len < 2 zeros will be used
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
