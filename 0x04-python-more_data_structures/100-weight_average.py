#!/usr/bin/python3
def weight_average(my_list=[]):
    mul = 0
    sum = 0
    for item in my_list:
        mul += item[0] * item[1]
        sum += item[1]
    return mul / sum
