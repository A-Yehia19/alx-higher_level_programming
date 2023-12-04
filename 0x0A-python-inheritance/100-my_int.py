#!/usr/bin/python3

"""Module that defines a class MyInt that inherits from int"""


class MyInt(int):
    """Class MyInt that inherits from int"""

    def __eq__(self, num):
        """Returns the opposite of the equality comparison"""
        return super().__ne__(num)

    def __ne__(self, num):
        """Returns the opposite of the non-equality comparison"""
        return super().__eq__(num)
