#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = a_dictionary.copy()
    for key, value_in_dict in new_dict.items():
        if value_in_dict == value:
            del a_dictionary[key]
    return a_dictionary
