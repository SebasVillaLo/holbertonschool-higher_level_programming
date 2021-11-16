#!/usr/bin/python3

def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")

    ListCart = ['?', '.', ':']

    i = 0
    while i < len(text):
        if text[i] in ListCart:
            print(text[i] + "\n")
            if i + 1 == len(text):
                break
            i += 1

            while text[i] == ' ':
                i += 1
        else:
            print(text[i], end='')
            i += 1
