#!/usr/bin/python3

"""Unittest for models/rectangle.py"""
import unittest
import contextlib
import io
from models.rectangle import Rectangle
from models.base import Base


class RectangleTest(unittest.TestCase):
    """Tests for rectangle class."""

    def setUp(self):
        """Resets __nb_objects"""
        Base._Base__nb_objects = 0

    def test_class_docstring(self):
        """Tests for the presence of a class docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_correct_id(self):
        """Tests for correct id assignment"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_width_validation(self):
        """Tests for width validation"""
        with self.assertRaises(TypeError):
            Rectangle("2", 2)
        with self.assertRaises(TypeError):
            Rectangle(True, 1)
        with self.assertRaises(TypeError):
            Rectangle(10.5, 1)
        with self.assertRaises(TypeError):
            Rectangle([2], 1)
        with self.assertRaises(TypeError):
            Rectangle(None, 1)
        with self.assertRaises(ValueError):
            Rectangle(-1, 1)
        with self.assertRaises(ValueError):
            Rectangle(0, 1)
        self.assertEqual(Rectangle(1, 1).width, 1)
        self.assertEqual(Rectangle(10, 1).width, 10)
        self.assertEqual(Rectangle(5, 1).width, 5)

    def test_height_validation(self):
        """Tests for height validation"""
        with self.assertRaises(TypeError):
            Rectangle(2, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, True)
        with self.assertRaises(TypeError):
            Rectangle(1, 10.5)
        with self.assertRaises(TypeError):
            Rectangle(1, [2])
        with self.assertRaises(TypeError):
            Rectangle(1, None)
        with self.assertRaises(ValueError):
            Rectangle(1, -1)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        self.assertEqual(Rectangle(1, 1).height, 1)
        self.assertEqual(Rectangle(1, 10).height, 10)
        self.assertEqual(Rectangle(1, 5).height, 5)

    def test_x_validation(self):
        """Tests for x validation"""
        with self.assertRaises(TypeError):
            Rectangle(2, 2, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 1, True)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 10.5)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, [2])
        with self.assertRaises(TypeError):
            Rectangle(1, 1, None)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1)
        self.assertEqual(Rectangle(1, 1, 0).x, 0)
        self.assertEqual(Rectangle(1, 1, 10).x, 10)
        self.assertEqual(Rectangle(1, 1, 5).x, 5)

    def test_y_validation(self):
        """Tests for y validation"""
        with self.assertRaises(TypeError):
            Rectangle(2, 2, 1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, True)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, 10.5)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, [2])
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, None)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 1, -1)
        self.assertEqual(Rectangle(1, 1, 1, 0).y, 0)
        self.assertEqual(Rectangle(1, 1, 1, 10).y, 10)
        self.assertEqual(Rectangle(1, 1, 1, 5).y, 5)

    def test_area(self):
        """Tests for area"""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(4, 10, 4, 5).area(), 40)
        self.assertEqual(Rectangle(8, 10, 0, 0, 12).area(), 80)

    def test_display(self):
        """Tests for display"""
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            Rectangle(2, 3).display()
        r1_output = "##\n##\n##\n"
        self.assertEqual(f.getvalue(), r1_output)

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            Rectangle(3, 2).display()
        r2_output = "###\n###\n"
        self.assertEqual(f.getvalue(), r2_output)

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            Rectangle(3, 2, 1, 0).display()
        r3_output = " ###\n ###\n"
        self.assertEqual(f.getvalue(), r3_output)

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            Rectangle(3, 2, 1, 1).display()
        r4_output = "\n ###\n ###\n"
        self.assertEqual(f.getvalue(), r4_output)

    def test_str(self):
        """Tests for __str__"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_update_args(self):
        """Tests for update with *args"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Tests for update with **kwargs"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_to_dictionary(self):
        """Tests for to_dictionary"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r1.to_dictionary(), r1_dictionary)
        r2 = Rectangle(1, 1)
        r2_dictionary = {'x': 0, 'y': 0, 'id': 2, 'height': 1, 'width': 1}
        self.assertEqual(r2.to_dictionary(), r2_dictionary)
        r3 = Rectangle(1, 1, 1, 1, 1)
        r3_dictionary = {'x': 1, 'y': 1, 'id': 1, 'height': 1, 'width': 1}
        self.assertEqual(r3.to_dictionary(), r3_dictionary)

if __name__ == '__main__':
    unittest.main()