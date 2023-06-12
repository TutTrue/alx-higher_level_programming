#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] == '+':
        print("{:d} {} {:d} = {:d}"
              .format(argv[1], argv[2], argv[3], add(argv[1], argv[2])))
    elif argv[2] == '-':
        print("{:d} {} {:d} = {:d}"
              .format(argv[1], argv[2], argv[3], sub(argv[1], argv[2])))
    elif argv[2] == '*':
        print("{:d} {} {:d} = {:d}"
              .format(argv[1], argv[2], argv[3], mul(argv[1], argv[2])))
    elif argv[2] == '/':
        print("{:d} {} {:d} = {:d}"
              .format(argv[1], argv[2], argv[3], div(argv[1], argv[2])))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
