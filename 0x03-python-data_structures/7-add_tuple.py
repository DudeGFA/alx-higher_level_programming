#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_list = []
    for i in range(2):
        firstval = tuple_a[i] if len(tuple_a) > i else 0
        secondval = tuple_b[i] if len(tuple_b) > i else 0
        new_list.append(firstval + secondval)
    return tuple(new_list)
