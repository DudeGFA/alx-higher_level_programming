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

    def area(self):
        "returns area of a rectangle"
        return self.__height * self.__width

    def perimeter(self):
        "returns perimeter of a rectangle"
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """returns # representaion of the rectangle"""
        if self.__width is 0 or self.__height is 0:
            return ""
        return ("\n".join("".join(["#" for i in range(self.__width)])
                for j in range(self.__height)))

    def __repr__(self):
        """returns string representaion of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """prints delete message"""
        print("Bye rectangle...")
