#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argumentos = len(sys.argv) - 1
    if argumentos == 0:
        print("0 arguments.")
    elif argumentos == 1:
        print("1 argument:")
        print("{}: {}".format(argumentos, sys.argv[argumentos]))
    else:
        print("{} arguments:".format(argumentos))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
