#!/usr/bin/python3
""""
def inherits_from
"""


def inherits_from(obj, a_class):
    """"implemet"""

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
