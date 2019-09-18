#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if (len(argv) != 4):
        print("./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    sign = argv[2]
    if (sign != "+" and sign != "-" and sign != "*" and sign != "/"):
        print("Unknown operator. Only: +, -, * and / available")
        exit(1)
    if (argv[2] == "-"):
        total = sub(int(argv[1]), int(argv[3]))
    if (argv[2] == "/"):
        total = div(int(argv[1]), int(argv[3]))
    if (argv[2] == "*"):
        total = mul(int(argv[1]), int(argv[3]))
    print("{} {} {} = {}".format(argv[1], argv[2], argv[3], total))
