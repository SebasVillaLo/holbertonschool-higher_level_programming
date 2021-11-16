#!/usr/bin/python3
""""
def json
"""
import json


def save_to_json_file(my_obj, filename):
    """"
    return
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
