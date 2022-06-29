#!/usr/bin/python3
a=0
b=0
for i in range(1, 80):
    if sorted(str(i)) == list(str(i)) and ((i // 10) != (i % 10)):
        print("{:02}".format(i), end=", ")
print("89")
