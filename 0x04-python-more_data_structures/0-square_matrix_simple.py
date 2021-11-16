#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newlist = []
    if len(matrix) > 0:
        for i in matrix:
            newlist.append(list(map(lambda j : j ** 2, i)))
    return newlist
	