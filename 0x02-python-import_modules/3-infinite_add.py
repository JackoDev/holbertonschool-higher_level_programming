#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    addition = 0
    count = 1
    while count < len(argv):
        addition = addition + int(argv[count])
        count = count + 1
    print(addition)
