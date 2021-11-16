#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    mylist = my_list
    if idx < 0 or idx > len(my_list) - 1:
        return mylist
    mylist = my_list[:]
    mylist[idx] = element
    return mylist
