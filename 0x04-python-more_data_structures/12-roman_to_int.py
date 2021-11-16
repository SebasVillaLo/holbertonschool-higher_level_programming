#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000}
    res = 0
    men = 0
    for i in roman_string:
        for j, x in romanos.items():
            if i == j:
                if men == 0 or men >= x:
                    res += x
                elif men < x:
                    res += x - (men*2)
                men = x
    return res
