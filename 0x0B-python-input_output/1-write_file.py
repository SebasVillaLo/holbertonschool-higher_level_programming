#!/usr/bin/python3
""""
def write file
"""


def write_file(filename="", text=""):
    """"
    write
    """
    count_lines = 0
    new_text = 0
    with open(filename, mode='w', encoding='utf-8') as f:
        new_text = f.write(text)
    return new_text
