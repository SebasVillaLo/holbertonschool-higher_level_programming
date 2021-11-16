#!/usr/bin/python3
if __name__ == '__main__':
from calculator_1 import add, sub, mul, div
import sys
    operaciones = {"+": add, "-": sub, "*": mul, "/": div}
    args = len(argv) - 1
    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op not in operaciones:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    res = operaciones[op](a, b)
    print("{} {} {} = {}".format(a, op, b, res))
