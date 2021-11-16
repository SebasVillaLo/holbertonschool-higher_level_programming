#!/usr/bin/python3
""""class square"""


class Square:
    """Defines a square:"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializer object"""

        self.__size = size
        self.__position = position

    def area(self):
        """return area of the Square in the atribute private __size"""

        return self.__size ** 2

    @property
    def size(self):
        """converts the private attribute"""

        return self.__size

    @size.setter
    def size(self, value):
        """assigns the value to the size variable"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                print("".join('#' for i in range(self.size)))

    @property
    def position(self):
        """makes the private """

        return self.__position

    @position.setter
    def position(self, value):
        """assigns the value to the position variable"""

        if type(value) is not tuple or len(value) > 1:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = value
