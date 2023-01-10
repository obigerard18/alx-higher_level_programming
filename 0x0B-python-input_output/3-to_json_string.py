#!/usr/bin/python3
"""Module for write_file method"""


def write_file(filename="", text=""):
    """
    Method that writes a string to a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as my_file_3:
        return my_file_3.write(text)
