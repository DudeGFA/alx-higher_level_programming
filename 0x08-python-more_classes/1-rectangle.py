#!/usr/bin/python3
# Author - God'sfavour Idowu-Agida

""" Definition of class Rectangle"""


class Rectangle:
    """ class Rectangle"""
    def __init__(self, width=0, height=0):
        """instantiation with optional attributes width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns rectangle width"""
        return self.__width

    @width.setter
    def width(self, new_width):
        """sets width"""
        if type(new_width) is not int:
            raise TypeError("width must be an integer")
        if new_width < 0:
            raise ValueError("width must be >= 0")
        self.__width = new_width

    @property
    def height(self):
        """returns rectangle height"""
        return self.__height

    @height.setter
    def height(self, new_height):
        """sets height"""
        if type(new_height) is not int:
            raise TypeError("height must be an integer")
        if new_height < 0:
            raise ValueError("height must be >= 0")
        self.__height = new_height
