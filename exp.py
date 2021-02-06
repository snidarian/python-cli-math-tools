#! /usr/local/bin/python3.9
# You might have to change above shebang line to path of your python interpreter

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("base", help="base (1st argument", type=float)
parser.add_argument("exponent", help="exponent (2nd argument", type=float)
parser.add_argument("-v", "--verbose", help="Verbose output", action="store_true")

args = parser.parse_args()
answer = args.base**args.exponent


if args.verbose:
  print(f"{args.base} to the power of {args.exponent} is equal to {answer}")
else:
  print(args.base**args.exponent)



  
  
  
  
