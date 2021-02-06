#! /usr/local/bin/python3.9
# this program generates random integers and displays them to stdout of command line terminal
# int_gen [generate n numbers] in range [n] to [n] - so the program takes three arguments

import random
import argparse

parser = argparse.ArgumentParser()


args = parser.add_argument("quantity", help="quantity of random integers", type=int)
args = parser.add_argument("start", help="begining of integer range", type=int)
args = parser.add_argument("end", help="ending of integer range", type=int)

args = parser.parse_args()

count = 0

while count < args.quantity:
    rand = random.randint(args.start, args.end)
    print(f"{rand}", end=" ")
    count += 1


print(end="\n")











