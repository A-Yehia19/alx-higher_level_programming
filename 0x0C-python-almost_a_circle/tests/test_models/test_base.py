#!/usr/bin/python3

"""Unittest for models/base.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class BaseTest(unittest.TestCase):
    """Tests for base class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_class_docstring(self):
        """Tests for the Base class docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_correct_id(self):
        """Tests for correct id assignment"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_to_json_string(self):
        """Tests for to_json_string method"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 1}]), '[{"id": 1}]')
        self.assertEqual(Base.to_json_string([{"id": 1}, {"id": 2}]),
                         '[{"id": 1}, {"id": 2}]')

    def test_from_json_string(self):
        """Tests for from_json_string method"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{"id": 1}])
        self.assertEqual(Base.from_json_string('[{"id": 1}, {"id": 2}]'),
                         [{"id": 1}, {"id": 2}])
        self.assertEqual(Base.from_json_string('[{"id": 1}, {"id": 2}, {"id": 3}]'),
                         [{"id": 1}, {"id": 2}, {"id": 3}])

    def test_create(self):
        """Tests for create method"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1 == r2, False)
        self.assertEqual(r1 is r2, False)
        self.assertEqual(r1.__str__() == r2.__str__(), True)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")

    def test_load_from_file(self):
        """Tests for load_from_file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(len(list_rectangles_output), 2)
        self.assertEqual(list_rectangles_output[0].__str__(), "[Rectangle] (1) 2/8 - 10/7")
        self.assertEqual(list_rectangles_output[1].__str__(), "[Rectangle] (2) 0/0 - 2/4")

    def test_save_to_file(self):
        """Tests for save_to_file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 105)

    def test_save_to_file_None(self):
        """Tests for save_to_file method with None"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty(self):
        """Tests for save_to_file method with empty list"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_more_args(self):
        """Tests for save_to_file method with more than one argument"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], [])



if __name__ == '__main__':
    unittest.main()