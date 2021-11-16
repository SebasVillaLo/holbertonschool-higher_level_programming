#!/usr/bin/python3
""""
class BaseGeometry
"""


class MyInt(int):
    """..."""

    def __eq__(self, another):
        """ ... """
        return self.real != another

    def __ne__(self, another):
        """..."""
        return self.real == another
