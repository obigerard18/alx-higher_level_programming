#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, 
    num_arg = len(sys.argv) - 1
    if num_arg < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a, operator, b = sys.argv[1:]
    if operator not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:s} {:s} {:s} = ".format(a, operator, b), end="")
    for ope, func in [('+', add), ('-', sub), ('*', mul), ('/', div)]:
        if operator == ope:
            print("{:d}".format(func(int(a), int(b))))
