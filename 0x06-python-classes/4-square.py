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

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square
        Args:
            value (int): new size of square to be set
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
