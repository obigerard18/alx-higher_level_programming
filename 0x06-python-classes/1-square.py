#!/usr/bin/python3
"Defines a class Square"


class Square:
    """Class Square that defines a square:
    -Private instance attribute: size
    -Instantiation with size (no type/value verification)"""
    def __init__(self, size):
        self.__size = size
