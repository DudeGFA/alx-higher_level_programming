#!/usr/bin/python3
# finds a peak element in a list
def findPeak(arr) :
    n = len(arr)
    if (n == 1) :
      return 0
    if (arr[0] >= arr[1]) :
        return 0
    if (arr[n - 1] >= arr[n - 2]) :
        return n - 1

    i = n - 1
    while i > 0 :
        if (arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]):
            return i
        elif (arr[i] > arr[i - 1]):
            i -= 1
        i -= 1