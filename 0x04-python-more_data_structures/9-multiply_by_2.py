#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict2 = a_dictionary.copy()
    for i, j in dict2.items():
        dict2[i] = j * 2
    return dict2
