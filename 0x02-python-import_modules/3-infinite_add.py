#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    suma = 0
    argumentos = len(sys.argv) - 1
    if argumentos == 0:
        print("0")
    else:
        for i in range(argumentos):
            suma = suma + int(sys.argv[i + 1])
        print("{}".format(suma))
