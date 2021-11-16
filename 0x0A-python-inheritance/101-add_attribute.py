#!/usr/bin/python3
""""
def add attri
"""

Rectangle = __import__('9-rectangle').Rectangle


def add_attribute(object, attr_name, value):
    """slots"""
    if "__slots__" in dir(object) or hasattr(object, "__dict__") is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
