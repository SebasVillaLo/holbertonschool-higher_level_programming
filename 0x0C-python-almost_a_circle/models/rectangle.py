#!/usr/bin/python3
""""
class rectangle
"""
from .base import Base


class Rectangle(Base):
    """"init"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """"init"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """"property"""
        return self.__width
    """"setter"""
    @width.setter
    def width(self, value):
        """"setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """"property"""
        return self.__height

    @height.setter
    def height(self, value):
        """"setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """"property"""
        return self.__x

    @x.setter
    def x(self, value):
        """"setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """"property"""
        return self.__y

    @y.setter
    def y(self, value):
        """"setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """"return"""
        return self.__height * self.__width

    def display(self):
        """"ciclo"""
        for y in range(self.__y):
            print("")
        for height in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for width in range(self.__width - 1):
                print('#', end="")
            print('#')

    def __str__(self):
        """"return"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """"condicional"""
        if len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.__width = arg
                if i == 2:
                    self.__height = arg
                if i == 3:
                    self.__x = arg
                if i == 4:
                    self.__y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]

    def to_dictionary(self):
        """"dict"""
        dict = {}

        dict["id"] = self.id
        dict["width"] = self.width
        dict["height"] = self.height
        dict["x"] = self.x
        dict["y"] = self.y

        return dict
