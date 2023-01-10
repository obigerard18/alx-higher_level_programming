#!/usr/bin/python3
"""Module for read_file method"""


def read_file(filename=""):
    """Method that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as my_file_0:
        print(my_file_0.read(), end="")
