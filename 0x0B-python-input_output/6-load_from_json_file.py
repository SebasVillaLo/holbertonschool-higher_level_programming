#!/usr/bin/python3
""""
def json
"""
import json


def load_from_json_file(filename):
    """"
    return
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
