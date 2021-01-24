#! /usr/local/bin/python3.9

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("base", help="base integer (1st argument", type=int)
parser.add_argument("exponent", help="exponent integer (2nd argument", type=int)

args = parser.parse_args()


print(args.base**args.exponent)



