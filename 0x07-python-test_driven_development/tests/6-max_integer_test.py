#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for unittest of max_integer program to test the function"""

    def test_documentation(self):
        self.assertTrue(len(__import__("6-max_integer").__doc__) > 0)

        self.assertTrue(len(max_integer.__doc__) > 0)

    def test_int(self):
        """Testing int numbers"""

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

        self.assertEqual(max_integer([-1, -2, 3, 4]), 4)

        self.assertEqual(max_integer([1]), 1)

        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_negatives(self):
        """ Testing negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_none(self):
        """Testing empties"""
        self.assertEqual(max_integer([]), None)

        self.assertEqual(max_integer(), None)

    def test_not_list(self):

        err_list = [1, 2, "three", 4]
        self.assertRaises(TypeError)

if __name__ == '__main__':
    unittest.main()
