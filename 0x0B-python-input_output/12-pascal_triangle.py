#!/usr/bin/python3
""""
def pascal
"""


def pascal_triangle(n):
    """"
    return pascal
    """
    if n <= 0:
        return []

    limit = n - 1
    triangle = [[1]]

    for i in range(limit):
        fila = []
        fila.append(1)

        if len(triangle[i]) > 1:
            largoprev = len(triangle[i]) - 1
            j2 = 1
            for j1 in range(largoprev):
                suma = triangle[i][j1] + triangle[i][j2]
                fila.append(suma)
                j2 += 1

        fila.append(1)
        triangle.append(fila)
    return triangle
