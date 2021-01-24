#! /usr/local/bin/python3.9
# change above shebang line to reflect absolute path to preffered python interpreter

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("square", help="Squares provided number", type=int)
parser.add_argument("-v", "--verbose", help="verbose output", action="store_true")

args = parser.parse_args()
answer = args.square**2

if args.verbose:
  print(f"{args.square} squared is equal to {answer}")
else:
  print(args.square**2)



