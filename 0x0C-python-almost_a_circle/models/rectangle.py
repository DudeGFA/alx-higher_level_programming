#!/usr/bin/python3
"""Contains class rectangle"""
from models.base import Base


class Rectangle(Base):
    """Represention of a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialises class rectangle
        Args:
            width (int): width of new rectangle
            height (int): height of new rectangle
            x (Int): The x coordinate of the new rectangle
            y (int): Y coordinate of the new rectangle
            id (int): identity no of the new Rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """depicts visual representation of a
        rectangle with # character"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for j in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print('#', end="") for i in range(self.width)]
            print("")

    def __str__(self):
        """returns the str() representation of the rectangle"""
        sp1 = "({}) {}/{} ".format(self.id, self.x, self.y)
        sp2 = "- {}/{}".format(self.width, self.height)
        return "[Rectangle] " + sp1 + sp2

    def update(self, *args, **kwargs):
        """Updates the rectangle's attributes
        Args:
            *args (ints): New attribute values.
                - 1st argument repressents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument reepresents x attribute
                - 5th argument represents y attribute
                **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__int__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of the rectangle"""
        return {"x": self.x, "y": self.y, "id": self.id,
                "height": self.height,
                "width": self.width
                }
