#!/usr/bin/python3
"""contains say_my_name"""


def say_my_name(first_name, last_name=""):
    """prints my name
    Args:
        first_name: my first name
        last_name: my last name
    Returns: nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
