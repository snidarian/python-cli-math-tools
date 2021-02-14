#! /usr/bin/python3
# Factorial recursive algorithm

import argparse


parser = argparse.ArgumentParser(description="Returns factorial of given integer argument")

args = parser.add_argument("intarg", help="Int to be factored", type=int)

args = parser.parse_args()


def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)



print(factorial_recursive(args.intarg))


