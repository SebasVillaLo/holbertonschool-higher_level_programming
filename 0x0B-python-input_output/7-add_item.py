#!/usr/bin/python3
""""
def json
"""
from sys import argv
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    list_j = load_from_json_file('add_item.json')
except:
    list_j = []

for count in range(1, len(argv)):
    list_j.append(argv[count])

save_to_json_file(list_j, 'add_item.json')
