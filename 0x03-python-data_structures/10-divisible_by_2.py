#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    even_list = []
    for num in my_list:
        even_list.append(num % 2 == 0)
    return even_list
