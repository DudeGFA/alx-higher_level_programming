#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_of_my_list = set(my_list)
    sum = 0
    for no in set_of_my_list:
        sum += no
    return sum
