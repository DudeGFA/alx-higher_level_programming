#!/usr/bin/python3
""" Contains function findPeak"""


def find_peak(list_of_integers):
    """Finds a peak element in a list"""

    n = len(list_of_integers)
    if (n == 1):
        return 0
    if (list_of_integers[0] >= list_of_integers[1]):
        return 0
    if (list_of_integers[n - 1] >= list_of_integers[n - 2]):
        return n - 1

    i = n - 1
    while i > 0:
        if (list_of_integers[i] >= list_of_integers[i - 1] and list_of_integers[i] >= list_of_integers[i + 1]):
            return i
        elif (list_of_integers[i] > list_of_integers[i - 1]):
            i -= 1
        i -= 1
