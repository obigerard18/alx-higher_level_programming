#!/usr/bin/python3
"""Module for Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Base and Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size of a rectangle"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Prints string representation of a Square"""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Public method: assigns an argument to each attribute"""
        attributes = ["id", "size", "x", "y"]
        for atrr, arg in zip(attributes, args):
            setattr(self, atrr, arg)
        for atrr, arg in kwargs.items():
            setattr(self, atrr, arg)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        attributes = ["id", "size", "x", "y"]
        return {key: getattr(self, key) for key in attributes}
