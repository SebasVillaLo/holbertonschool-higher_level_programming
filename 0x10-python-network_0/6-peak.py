#!/usr/bin/python3
"""search the peak"""


def find_peak(list_of_integers):
    """search the peak"""
    long = len(list_of_integers)

    if not list_of_integers:
        return None

    return funcion(list_of_integers, 0, long - 1)


def funcion(list, start, end):
    """search the peak"""
    mid = int((start + end) / 2)

    if mid + 1 >= len(list) or list[mid + 1] <= list[mid]:
        if mid - 1 < 0 or list[mid - 1] <= list[mid]:
            return list[mid]
        else:
            return funcion(list, 0, mid)
    else:
        return funcion(list, mid + 1, end)
