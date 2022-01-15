#!/usr/bin/python3
"""
Divide numbers in matrix. Round to 2 decimal places.
"""

def matrix_divided(matrix, div):
    """
    Raise errors if necessary
    """
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(matrix, (list)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(x) == len(matrix[0]) for x in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(len(x) > 0 for x in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return(list(round(y / div, 2) for z in matrix for y in z if div != 0))
