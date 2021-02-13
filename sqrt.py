#! /usr/local/bin/python3.9
# takes single float/int command line argument and displays its square root

import argparse
import math

parser = argparse.ArgumentParser(description='Print square root of single number.')

args = parser.add_argument("float", help="Number to take square root of", type=float)
args = parser.add_argument("-v", "--verbose", help="Verbose flag option", action="store_true")

args = parser.parse_args()

result = 0

if args.float and args.verbose:
    result = math.sqrt(args.float)
    print("The square root of " + str(args.float) + " is " + str(result))
elif args.float:
    result = math.sqrt(args.float)
    print(result)
else:
    print("Argument error: --help to print help message")




















