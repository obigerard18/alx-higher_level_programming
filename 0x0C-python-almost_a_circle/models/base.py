#!/usr/bin/python3
"""Module for Base class"""
from json import dumps, loads
import csv
from os import path


class Base:
    """This is a “base” class of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        
        @staticmethod
        def to_json_string(list_dictionaries):
            """returns the JSON string representation of list_dictionaries"""
            if not list_dictionaries or not len(list_dictionaries):
                list_dictionaries = []
            return dumps(list_dictionaries)

        @classmethod
        def save_to_file(cls, list_objs):
            """writes the JSON string representation of list_objs to a fil"""
            if not list_objs:
                list_objs = []
            list_objs = [obj.to_dictionary() for obj in list_objs]
            with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
                f.write(cls.to_json_string(list_objs))

        @staticmethod
        def from_json_string(json_string):
            """ returns the list of the JSON string representation json_string"""
            if json_string is None or not json_string:
                return []
            return loads(json_string)

        @classmethod
        def create(cls, **dictionary):
            """returns an instance with all attributes already set"""
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            elif cls.__name__ == "Square":
                new = cls(1)
            else:
                new = None
            new.update(**dictionary)
            return new

        @classmethod
        def load_from_file(cls):
            """returns a list of instances (convert json representations)"""
            file_load = "{}.json".format(cls.__name__)
            if not path.isfile(file_load):
                return []
            with open(file_load, "r", encoding="utf-8") as f:
                return[cls.create(**dic) for dic in cls.from_json_string(f.read())]

        @classmethod
        def save_to_file_csv(cls, list_objs):
            """Converts 'list_objs' to csv format"""
            if not list_objs:
                list_objs = []
            with open("{}.csv".format(cls.__name__), 'w', encoding="utf-8") as fil:
                if cls.__name__ == "Rectangle":
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == "Square":
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(fil, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

        @classmethod
        def load_from_file_csv(cls):
            """Loads file containing csv representation"""
            list_objs = []
            with open("{}.csv".format(cls.__name__), 'r') as file_csv:
                if cls.__name__ == "Rectangle":
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == "Square":
                    fields = ['id', 'size', 'x', 'y']
                reader = csv.DictReader(file_csv, fieldnames=fields)
                list_objs = []
                for row in reader:
                    for key in row:
                        row[key] = int(row[key])
                    list_objs.append(cls.create(**row))
            return list_objs
