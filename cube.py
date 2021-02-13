#! /usr/local/bin/python3.9
# Cubes single number and outputs to screen

import argparse

parser = argparse.ArgumentParser(description='Cubes a number.')

args = parser.add_argument("cube", help="Positional Number to be cubed", type=float)
args = parser.add_argument("-v", "--verbose", help="verbose output", action="store_true")

args = parser.parse_args()

result = 0

if args.cube and args.verbose:
    result = args.cube**3
    print(str(args.cube) + " cubed is " + str(result))
elif args.cube:
    result = args.cube**3
    print(result)
else:
    print("Error: Supply float/integer to be cubed")










