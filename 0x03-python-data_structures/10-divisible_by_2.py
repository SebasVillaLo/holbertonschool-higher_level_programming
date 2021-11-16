#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mylist = []
    for i, info in enumerate(my_list):
        if info % 2 == 0:
            mylist.append(True)
        else:
            mylist.append(False)
    return mylist
