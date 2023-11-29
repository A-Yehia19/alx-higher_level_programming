#!/usr/bin/python3

"""Module that multiplies 2 matrices using the module NumPy"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices using the module NumPy"""
    return numpy.matmul(m_a, m_b)
