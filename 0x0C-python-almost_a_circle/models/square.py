#!/usr/bin/python3
"""Contains class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new square.

        Args:
            size (int): The size of the new square.
            x (int): The x coordinate of the new Square.
            y (Int): The y coordinate of the new square
            id (int): the identity of the new square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter of square size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter of square size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square attributes
        Args:
            *args (ints): New attribute values
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument repressents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
            """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__int__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        sw = self.width
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, sw)

    def to_dictionary(self):
        """returns dictionary representation of a square instance"""
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
