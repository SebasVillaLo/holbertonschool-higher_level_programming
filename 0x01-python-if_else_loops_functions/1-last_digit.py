#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
p1 = "Last digit of"
if number >= 0:
    mod = number % 10
else:
    mod = number % -10
if mod > 5:
    print("{} {} is {} and is greater than 5".format(p1, number, mod))
elif mod == 0:
    print("{} {} is {} and is 0".format(p1, number, mod))
elif mod < 6 and mod != 0:
    print("{} {} is {} and is less than 6 and not 0".format(p1, number, mod))
