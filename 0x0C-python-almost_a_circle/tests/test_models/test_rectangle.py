#!/usr/bin/python3
"""Module for Rectangle unit tests"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import io
from models.rectangle import __doc__ as doc_check
from contextlib import redirect_stdout


class TestRectangle(unittest.TestCase):
    """Test the Rectangle Class"""

    def setUp(self):
        """Initialize nb_objects before each test"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Cleans up tasks"""
        pass

    def test_docstrings(self):
        self.assertIsNotNone(doc_check)
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIs(hasattr(Rectangle, "__init__"), True)
        self.assertIsNotNone(Rectangle.__init__.__doc__)
        self.assertIs(hasattr(Rectangle, "width"), True)
        self.assertIsNotNone(Rectangle.width.__doc__)
        self.assertIs(hasattr(Rectangle, "height"), True)
        self.assertIsNotNone(Rectangle.height.__doc__)
        self.assertIs(hasattr(Rectangle, "x"), True)
        self.assertIsNotNone(Rectangle.x.__doc__)
        self.assertIs(hasattr(Rectangle, "y"), True)
        self.assertIsNotNone(Rectangle.y.__doc__)
        self.assertIs(hasattr(Rectangle, "area"), True)
        self.assertIsNotNone(Rectangle.area.__doc__)
        self.assertIs(hasattr(Rectangle, "display"), True)
        self.assertIsNotNone(Rectangle.display.__doc__)
        self.assertIs(hasattr(Rectangle, "__str__"), True)
        self.assertIsNotNone(Rectangle.__str__.__doc__)
        self.assertIs(hasattr(Rectangle, "update"), True)
        self.assertIsNotNone(Rectangle.update.__doc__)
        self.assertIs(hasattr(Rectangle, "to_dictionary"), True)
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)

# ---------------Tests: task 2 and 3--------------------------------
    def test_class(self):
        """Test Rectangle class"""
        self.assertEqual(str(Rectangle), "<class 'models.rectangle.\
Rectangle'>")

    def test_inheritance(self):
        """Test if Rectangle inherits from Base"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_init_no_args(self):
        """Test Rectangle() instantiation without self"""
        with self.assertRaises(TypeError) as excep:
            Rect_test = Rectangle()
        message = "__init__() missing 2 required positional \
arguments: 'width' and 'height'"
        self.assertEqual(str(excep.exception), message)

    def test_init_one_arg(self):
        """Test Rectangle() instantiation with a missing argument"""
        with self.assertRaises(TypeError) as excep:
            Rect_test = Rectangle(67)
        message = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(excep.exception), message)

    def test_init_excedent_args(self):
        """Test Rectangle() instantiation with leftover arguments"""
        with self.assertRaises(TypeError) as excep:
            Rect_test = Rectangle(45, 56, 89, 102, 56, 23)
        message = "__init__() takes from 3 to 6 positional \
arguments but 7 were given"
        self.assertEqual(str(excep.exception), message)

    def test_instantiation(self):
        """Test Rectangle() instantiation with 2 arguments"""
        Rect_test = Rectangle(6, 8)
        self.assertEqual(str(type(Rect_test)), "<class 'models.\
rectangle.Rectangle'>")
        self.assertTrue(isinstance(Rect_test, Base))
        dic = {'_Rectangle__height': 8,
               '_Rectangle__width': 6,
               '_Rectangle__x': 0,
               '_Rectangle__y': 0,
               'id': 1}
        self.assertEqual(Rect_test.__dict__, dic)

    def test_instantiation_positional(self):
        """Test Rectangle() positional instantiation"""
        Rect_test = Rectangle(9, 4, 12, 7, 8)
        self.assertEqual(str(type(Rect_test)), "<class 'models.\
rectangle.Rectangle'>")
        self.assertTrue(isinstance(Rect_test, Base))
        dic = {'_Rectangle__height': 4,
               '_Rectangle__width': 9,
               '_Rectangle__x': 12,
               '_Rectangle__y': 7,
               'id': 8}
        self.assertEqual(Rect_test.__dict__, dic)

        Rect_test = Rectangle(5, 7, 19, 2)
