#!/usr/bin/python3
"""Module for class student"""


class Student:
    """Class that defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary"""
        if type(attrs) is list and all(type(t) is str for t in attrs):
            return {ky: vl for ky, vl in self.__dict__.items() if ky in attrs}
        else:
            return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            self.__dict__[key] = value
