#!/usr/bin/python3
"""Class MagicClass"""
import math


class MagicClass:
    """Magic Class"""
    def _init(self, radius=0):
        """Initialize MagicClass"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """Calculate area of circle"""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Calculate circumference of circle"""
        return 2 * math.pi * self._MagicClass__radius
