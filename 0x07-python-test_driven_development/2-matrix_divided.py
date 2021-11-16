#!/usr/bin/python3
"""
Function that divides
Return matrix
"""


def matrix_divided(matrix, div):
    """
    Divides matrix
    """

    if div is None:
        raise TypeError("div must be a number")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    """Check if the matrix is a list of integers and floats"""
    mess_1 = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(mess_1)
    for rows in matrix:
        if type(rows) is not list:
            raise TypeError(mess_1)
        for column in rows:
            if type(column) not in (int, float):
                raise TypeError(mess_1)

    """Check rows of matrix should be the same size"""
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    """Divide index by div value"""
    newlist = []
    for row in matrix:
        newlist.append(list(map(lambda x: round(x / div, 2), row)))
    return newlist
