#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """representaion of a square"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize a new Square.
        Args:
            size (int): size of square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

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

    def my_print(self):
        """prints a square."""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            for i in range(self.__size):
                print("#", end="")
            print("")

    @property
    def position(self):
        """returns position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        ERR = "position must be a tuple of 2 positive integers"
        if value is not tuple or len(value) != 2:
            raise TypeError(ERR)
        for num in value:
            if num is not int or num < 0:
                raise TypeError(ERR)
        __position = value
