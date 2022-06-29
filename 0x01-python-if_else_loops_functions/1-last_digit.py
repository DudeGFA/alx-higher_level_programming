#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ber = number % 10
if number < 0:
    ber = -1*((number * (-1)) % 10)
if ber > 5:
    print(f"Last digit of {number} is {ber} and is greater than 5")
elif ber == 0:
    print(f"Last digit of {number} is {ber} and is 0")
else:
    print(f"Last digit of {number} is {ber} and is less than 6 and not 0")
