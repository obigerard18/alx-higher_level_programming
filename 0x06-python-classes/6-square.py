#!/usr/bin/python3
"Defines a class Square"


class Square:
    """Class Square that defines a square

    Attributes:
    __size (int): size of a size of the square
    __position (tuple): position of the square in 2D"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return(self.__size)

    @property
    def position(self):
        return(self.__position)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) is not 2 or \
                type(value[0]) is not int or value[0] < 0 or \
                type(value[1]) is not int or value[1] < 0:
                  raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    
    def area(self):
        return(self.__size**2)

    def my_print(self):
        if self.__size is 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
