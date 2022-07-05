#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    maxval = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > maxval:
            maxval = my_list[i]
    return maxval
