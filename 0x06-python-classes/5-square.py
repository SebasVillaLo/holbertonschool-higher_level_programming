#!/usr/bin/python3
""""class square"""


class Square:
    """Define Square"""

    def __init__(self, size=0):
        """"Objetos"""

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
    """Print a square #"""

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                print("".join('#' for i in range(self.size)))
    """Return"""

    def area(self):
        return self.__size ** 2
