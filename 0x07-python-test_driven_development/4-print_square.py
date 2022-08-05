#!/usr/bin/python3
"""contains print_square"""

def print_square(size):
    """Prints a square using #
    Args:
        size (int): size of square
    Raises:
        TypeError: if size is not an int
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
