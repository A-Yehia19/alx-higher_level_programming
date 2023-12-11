#!/usr/bin/python3

"""Unittest for models/square.py"""
import unittest
import io
import contextlib
from models.square import Square
from models.base import Base


class SquareTest(unittest.TestCase):
    """Tests for square class."""

    def setUp(self):
        """Resets __nb_objects"""
        Base._Base__nb_objects = 0

    def test_class_docstring(self):
        """Tests for the presence of a class docstring"""
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_correct_id(self):
        """Tests for correct id assignment"""
        s1 = Square(10)
        s2 = Square(2)
        s3 = Square(10, 0, 0, 12)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 12)

    def test_size_validation(self):
        """Tests for size validation"""
        with self.assertRaises(TypeError):
            Square("2")
        with self.assertRaises(TypeError):
            Square(True)
        with self.assertRaises(TypeError):
            Square(10.5)
        with self.assertRaises(TypeError):
            Square([2])
        with self.assertRaises(TypeError):
            Square(None)
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(0)
        self.assertEqual(Square(1).size, 1)
        self.assertEqual(Square(10).size, 10)
        self.assertEqual(Square(5).size, 5)

    def test_x_validation(self):
        """Tests for x validation"""
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, True)
        with self.assertRaises(TypeError):
            Square(1, 10.5)
        with self.assertRaises(TypeError):
            Square(1, [2])
        with self.assertRaises(TypeError):
            Square(1, None)
        with self.assertRaises(ValueError):
            Square(1, -1)
        self.assertEqual(Square(1, 0).x, 0)
        self.assertEqual(Square(1, 10).x, 10)
        self.assertEqual(Square(1, 5).x, 5)

    def test_y_validation(self):
        """Tests for y validation"""
        with self.assertRaises(TypeError):
            Square(1, 1, "2")
        with self.assertRaises(TypeError):
            Square(1, 1, True)
        with self.assertRaises(TypeError):
            Square(1, 1, 10.5)
        with self.assertRaises(TypeError):
            Square(1, 1, [2])
        with self.assertRaises(TypeError):
            Square(1, 1, None)
        with self.assertRaises(ValueError):
            Square(1, 1, -1)
        self.assertEqual(Square(1, 1, 0).y, 0)
        self.assertEqual(Square(1, 1, 10).y, 10)
        self.assertEqual(Square(1, 1, 5).y, 5)

    def test_area(self):
        """Tests for area method"""
        self.assertEqual(Square(3).area(), 9)
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(7, 0, 0, 12).area(), 49)

    def test_display(self):
        """Tests for display method"""
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            Square(5).display()
        r1_output = "#####\n#####\n#####\n#####\n#####\n"
        self.assertEqual(f.getvalue(), r1_output)

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            Square(2, 2).display()
        r2_output = "  ##\n  ##\n"
        self.assertEqual(f.getvalue(), r2_output)

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            Square(3, 1, 3).display()
        r3_output = "\n\n\n ###\n ###\n ###\n"
        self.assertEqual(f.getvalue(), r3_output)

    def test_str(self):
        """Tests for __str__ method"""
        s1 = Square(4, 2, 1, 12)
        self.assertEqual(str(s1), "[Square] (12) 2/1 - 4")
        s2 = Square(5, 1, 0)
        self.assertEqual(str(s2), "[Square] (1) 1/0 - 5")

    def test_update_args(self):
        """Tests for update method with *args"""
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """Tests for update method with **kwargs"""
        s1 = Square(5)
        s1.update(size=10)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")
        s1.update(size=1, x=2)
        self.assertEqual(str(s1), "[Square] (1) 2/0 - 1")
        s1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(str(s1), "[Square] (89) 3/1 - 2")
        s1.update(x=1, size=2, y=3)
        self.assertEqual(str(s1), "[Square] (89) 1/3 - 2")

    def test_to_dictionary(self):
        """Tests for to_dictionary method"""
        s1 = Square(10, 2, 1)
        s1_dictionary = {'x': 2, 'y': 1, 'id': 1, 'size': 10}
        self.assertEqual(s1.to_dictionary(), s1_dictionary)
        s2 = Square(1, 1)
        s2_dictionary = {'x': 1, 'y': 0, 'id': 2, 'size': 1}
        self.assertEqual(s2.to_dictionary(), s2_dictionary)
        s3 = Square(1, 1, 1, 1)
        s3_dictionary = {'x': 1, 'y': 1, 'id': 1, 'size': 1}
        self.assertEqual(s3.to_dictionary(), s3_dictionary)

if __name__ == '__main__':
    unittest.main()