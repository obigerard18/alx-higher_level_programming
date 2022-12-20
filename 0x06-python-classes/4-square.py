#!/usr/bin/python3
"Defines a class Square"


class Square:
    """Class Square that defines a square

    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return(self.__size**2)
