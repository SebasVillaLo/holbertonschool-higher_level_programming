#!/usr/bin/python3
def no_c(my_string):
    characters = "Cc"
    mystring = ''
    for i in my_string:
        if i not in characters:
            mystring += i
    return mystring
