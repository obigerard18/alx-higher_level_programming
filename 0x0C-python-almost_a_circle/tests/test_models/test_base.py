#!/usr/bin/python3
"""Module for Base unit tests"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from models.base import __doc__ as doc_check
import json
import os


class TestBase(unittest.TestCase):
    """Test the Base Class"""

    def setUp(self):
        """Initialize nb_objects before each test"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Cleans up tasks"""
        pass

    def test_docstrings(self):
        self.assertIsNotNone(doc_check)
        self.assertIsNotNone(Base.__doc__)
        self.assertIs(hasattr(Base, "__init__"), True)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIs(hasattr(Base, "create"), True)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIs(hasattr(Base, "to_json_string"), True)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIs(hasattr(Base, "from_json_string"), True)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIs(hasattr(Base, "save_to_file"), True)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIs(hasattr(Base, "load_from_file"), True)
        self.assertIsNotNone(Base.load_from_file.__doc__)
        self.assertIs(hasattr(Base, "save_to_file_csv"), True)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIs(hasattr(Base, "load_from_file_csv"), True)
        self.assertIsNotNone(Base.load_from_file.__doc__)

# ---------------Tests: task 1 --------------------------------
    def test_nb_is_private(self):
        """Test if nb_objects is private instance attribute"""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_initialization(self):
        """Test if nb_objects initializes to 0"""
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_instantiation(self):
        """Test Base() instantiation"""
        Btest = Base()
        self.assertEqual(str(type(Btest)), "<class 'models.base.Base'>")
        self.assertEqual(Btest.__dict__, {"id": 1})
        self.assertEqual(Btest.id, 1)

    def test_init_no_args(self):
        """Test Base() instantiation without self"""
        with self.assertRaises(TypeError) as excep:
            Base.__init__()
        message = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excep.exception), message)

    def test_excedent__args(self):
        """Test Base() instantiation with leftover arguments"""
        with self.assertRaises(TypeError) as excep:
            Base.__init__(self, 12, 56)
        message = "__init__() takes from 1 to 2 positional arguments \
but 3 were given"
        self.assertEqual(str(excep.exception), message)

    def test_count_obj_no_id(self):
        """Test consecutives ids"""
        Btest1 = Base()
        Btest2 = Base()
        self.assertEqual(Btest2.id, Btest1.id + 1)

    def test_count_obj_id(self):
        """Test synchronous between instance and class id"""
        Btest1 = Base()
        Btest2 = Base(24)
        self.assertEqual(Btest2.id, 24)

    def test_class_inst_id(self):
        """Test synchronous between instance and class id"""
        Btest = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), Btest.id)
        Btest = Base()
        Btest = Base("betty")
        Btest = Base(56)
        Btest = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), Btest.id)

    def test_int_variable(self):
        """Test id dependent on a variable"""
        num = 56
        Btest = Base(num)
        self.assertEqual(Btest.id, num)

    def test_int_variable(self):
        """Test id dependent on a variable"""
        string = "holberton"
        Btest = Base(string)
        self.assertEqual(Btest.id, string)

    def test_key_word(self):
        """Test id dependent on a variable (with tag)"""
        num = 6
        Btest = Base(id=num)
        self.assertEqual(Btest.id, num)

# ---------------Tests: task 15 --------------------------------
    def test_json_string(self):
        """Test to_json_string method"""
        with self.assertRaises(TypeError) as excep:
            Base.to_json_string()
        message = "to_json_string() missing 1 required positional argument: \
'list_dictionaries'"
        self.assertEqual(str(excep.exception), message)

        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")
        dic = [{}]
        self.assertEqual(Base.to_json_string(dic), '[{}]')
        dic = [{}, {}, {}]
        self.assertEqual(Base.to_json_string(dic), '[{}, {}, {}]')

        dic = [{'width': 657, 'height': 78, 'x': 543, 'y': 965, 'id': 345}]
        self.assertEqual(len(Base.to_json_string(dic)), len(str(dic)))

        dic = [{'width': 65, 'height': 8, 'x': 3, 'y': 5, 'id': 34},
                {'width': 5, 'height': 1, 'x': 2, 'y': 6, 'id': 75}]
        self.assertEqual(len(Base.to_json_string(dic)), len(str(dic)))

        dic = [{'th': 7}, {'holberton': 3}]
        dic_json = '[{"th": 7}, {"holberton": 3}]'
        self.assertEqual(Base.to_json_string(dic), dic_json)

        dic = [{'help': 7}]
        dic_json = '[{"help": 7}]'
        self.assertEqual(Base.to_json_string(dic), dic_json)

        Rect_test = Rectangle(9, 54, 3, 1)
        dic = Rect_test.to_dictionary()
        json_dic = Base.to_json_string([dic])
        dic = str([dic])
        dic = dic.replace("'", '"')
        self.assertEqual(dic, json_dic)

        Rect_test1 = Rectangle(5, 6, 2, 9)
        Rect_test2 = Rectangle(78, 16, 9, 1)
        dic = [Rect_test1.to_dictionary(), Rect_test2.to_dictionary()]
        json_dic = Base.to_json_string([dic])
        dic = str([dic])
        dic = dic.replace("'", '"')
        self.assertEqual(dic, json_dic)

        Square_test = Square(54, 3, 1)
        dic = Square_test.to_dictionary()
        json_dic = Base.to_json_string([dic])
        dic = str([dic])
        dic = dic.replace("'", '"')
        self.assertEqual(dic, json_dic)

        Square_test1 = Square(5, 2, 9)
        Square_test2 = Square(16, 9, 1)
        dic = [Square_test1.to_dictionary(), Square_test2.to_dictionary()]
        json_dic = Base.to_json_string([dic])
        dic = str([dic])
        dic = dic.replace("'", '"')
        self.assertEqual(dic, json_dic)

# ---------------Tests: task 16 --------------------------------
    def test_save_to_file(self):
        '''Tests save_to_file() method.'''
        import os
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 105)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 52)

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except:
            pass
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        r2 = Square(1)
        Square.save_to_file([r2])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 38)

# ---------------Tests: task 17 --------------------------------
    def test_from_json_string(self):
        """Test from_json_string method"""
        with self.assertRaises(TypeError) as excep:
            Base.from_json_string()
        message = "from_json_string() missing 1 required positional argument: \
'json_string'"
        self.assertEqual(str(excep.exception), message)

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        string = '[{"x": 2, "y": 89, "width": 5, "id": 10, "height": 8}, \
{"x": 4, "y": 19, "width": 7, "id": 13, "height": 9}]'

        dic = [{'x': 2, 'y': 89, 'width': 5, 'id': 10, 'height': 8},
                {'x': 4, 'y': 19, 'width': 7, 'id': 13, 'height': 9}]

        self.assertEqual(Base.from_json_string(string), dic)

        string = '[{}]'
        dic = [{}]
        self.assertEqual(Base.from_json_string(string), dic)

        string = '[{"hol": 5, "ber": 9, "ton": 11, "is": 1, "awesome": 6}, \
{"a": 4, "b": 19, "c": 7, "d": 13, "e": 9}]'

        dic = [{'hol': 5, 'ber': 9, 'ton': 11, 'is': 1, 'awesome': 6},
                {'a': 4, 'b': 19, 'c': 7, 'd': 13, 'e': 9}]

        self.assertEqual(Base.from_json_string(string), dic)

        list_rect = [{'width': 2, 'height': 5, 'id': 3},
                     {'width': 2, 'height': 5, 'id': 3}]

        list_rev = Rectangle.from_json_string(
            Rectangle.to_json_string(list_rect))
        self.assertEqual(list_rect, list_rev)

        list_square = [{'size': 5, 'id': 3},
                       {'size': 2, 'id': 5}]

        list_rev = Square.from_json_string(
            Square.to_json_string(list_square))
        self.assertEqual(list_square, list_rev)

# ---------------Tests: task 18 --------------------------------
    def test_create(self):
        """Test create method"""
        Rect_test1 = Rectangle(2, 4, 2, 1)
        Rect_dic1 = Rect_test1.to_dictionary()
        Rect_test2 = Rectangle.create(**Rect_dic1)
        self.assertEqual(str(Rect_test1), str(Rect_test2))
        self.assertFalse(Rect_test1 is Rect_test2)
        self.assertFalse(Rect_test1 == Rect_test2)

        Square_test1 = Square(2)
        Square_dic1 = Square_test1.to_dictionary()
        Square_test2 = Square.create(**Square_dic1)
        self.assertEqual(str(Square_test1), str(Square_test2))
        self.assertFalse(Square_test1 is Square_test2)
        self.assertFalse(Square_test1 == Square_test2)

# ---------------Tests: task 19 --------------------------------
    def test_load_from_file(self):
        """Test load_from_file method"""
        Rect_test1 = Rectangle(7, 8)
        Rect_test2 = Rectangle(2, 4, 8, 9)
        list_input = [Rect_test1, Rect_test2]
        Rectangle.save_to_file(list_input)
        list_output = Rectangle.load_from_file()
        self.assertEqual(str(list_input[0]), str(list_output[0]))
        self.assertNotEqual(id(list_input[0]), id(list_output[0]))
        self.assertEqual(str(list_input[1]), str(list_output[1]))
        self.assertNotEqual(id(list_input[1]), id(list_output[1]))

        Square_test1 = Square(7, 8)
        Square_test2 = Square(2)
        list_input = [Square_test1, Square_test2]
        Square.save_to_file(list_input)
        list_output = Square.load_from_file()
        self.assertEqual(str(list_input[0]), str(list_output[0]))
        self.assertNotEqual(id(list_input[0]), id(list_output[0]))
        self.assertEqual(str(list_input[1]), str(list_output[1]))
        self.assertNotEqual(id(list_input[1]), id(list_output[1]))

if __name__ == "__main__":
    unittest.main()
