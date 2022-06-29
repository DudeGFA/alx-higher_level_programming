#!/usr/bin/python3

def uppercase(str):
    for d in str:
        if ord(d) >= 97 and ord(d) <= 122:
            d = chr(ord(d) - 32)
        print("{}".format(d), end="")
    print("")
