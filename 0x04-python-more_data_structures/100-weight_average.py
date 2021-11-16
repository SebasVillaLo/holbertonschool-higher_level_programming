#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    return sum([multi(x[0], x[1]) for x in my_list]) / sum(x[1] for x in my_list)

def multi(a, b):
    return a * b
