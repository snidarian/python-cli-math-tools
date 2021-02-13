#! /usr/local/bin/python3.9
# outputs the sum total of a list of command line arguments

import argparse

parser = argparse.ArgumentParser(description="Prints total of a list of command line number arguments")


args = parser.add_argument("numbers", help="Numbers to be totaled", nargs="*", type=float)
args = parser.add_argument("-v", "--verbose", help="Verbose option", action="store_true")

args = parser.parse_args()

result = 0

for x in args.numbers:
    result += x

if args.numbers and args.verbose:
    print("Sum = " + str(result))
elif args.numbers:
    print(str(result))
else:
    print("Argument error: --help to display help message")




