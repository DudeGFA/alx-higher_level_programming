#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """representaion of a square"""
    def __init__(self, size=0):
        """initialize a new Square.
        Args:
            size (int): size of square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """returns area of a square"""
        return self.__size ** 2
