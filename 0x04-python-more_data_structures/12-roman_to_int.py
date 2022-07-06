#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    sum = 0
    i = 0
    roman_dict = \
        {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    roman_dict_9 = {"IX": 9, "XC": 90, "CM": 900}
    while i < len(roman_string):
        if roman_string[i:i+2] in roman_dict_9:
            sum += roman_dict_9[roman_string[i:i+2]]
            i += 1
        elif roman_string[i] in roman_dict:
            sum += roman_dict[roman_string[i]]
        else:
            return (0)
        i += 1
    return (sum)
