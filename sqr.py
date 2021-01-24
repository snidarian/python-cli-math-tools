#! /usr/local/bin/python3.9
# change above shebang line to reflect absolute path to preferred python interpreter

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("square", type=int, help="display square of given number")
parser.add_argument("-v", "--verbose", type=int, help="increase output verbosity", choices=[0, 1, 2])

args = parser.parse_args()
answer = args.square**2

if args.verbose == 2:
    print(f"The square of {args.square} is {answer}")
elif args.verbose == 1:
    print(f"{args.square}^2 == {answer}")
else:
    print(answer)




