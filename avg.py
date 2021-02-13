#! /usr/local/bin/python3.9
# Take the average of a list of command line arguments and prints it to screen

import argparse

parser = argparse.ArgumentParser(description="Prints average of a list of command line number arguments")


args = parser.add_argument("numbers", help="Numbers to be averages", nargs="*", type=float)
args = parser.add_argument("-v", "--verbose", help="Verbose option", action="store_true")

args = parser.parse_args()

result = 0
argc = 0

for x in args.numbers:
    result += x
    argc += 1
if args.numbers and args.verbose:
    print("Sum = " + str(result))
    print("Average = " + str(result/argc))
    print("Argc = " + str(argc))
elif args.numbers:
    print(str(result/argc))
else:
    print("Argument error: --help to display help message")
