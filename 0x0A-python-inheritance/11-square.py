#!/usr/bin/python3
""""
class Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """return"""
        return super().area()

    def __str__(self):
        """return"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
