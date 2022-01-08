#!/usr/bin/python3
"""search the peak"""


def find_peak(list_of_integers):
    """this is the funtion for search peak"""
    long = len(list_of_integers)

    if not list_of_integers:
        return None

    for idx, i in enumerate(list_of_integers):

        if long <= 6:
            if idx == 0:
                idx = 1
            if i > list_of_integers[idx - 1] and i > list_of_integers[idx + 1]:
                return i

        if i > list_of_integers[idx - 1] and i > list_of_integers[idx + 1]:
            return i

    return list_of_integers[len(list_of_integers) - 1]
