#!/usr/bin/python3
""""
def read file
"""


def append_write(filename="", text=""):
    """"
    def read file
    """
    new_text = 0
    with open(filename, mode='a', encoding='utf-8') as f:
        new_text = f.write(text)
    return new_text
