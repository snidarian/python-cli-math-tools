#!/usr/bin/python3

"""
Program will return sample standard deviation, sample variance, average (with -v flag),
and margin of error (upon request with -m flag)
"""

import math
import argparse

parser = argparse.ArgumentParser(description='Calculates Sample standard deviation and variance.')

args = parser.add_argument("sample", help="help message", nargs="*", type=float)
args = parser.add_argument("-m", "--margin-of-error", help="Outputs margin of error", action="store_true")
args = parser.add_argument("-v", "--verbose", help="Verbose output", action="store_true")
# A flag and positional argument for calculating confidence level

args = parser.parse_args()

mean = 0
total = 0
variance = 0
std_dev = 0
argc = 0
sum_of_squares = 0
# calc element count and mean
for x in args.sample:
    total += x
    argc += 1

mean = (total/argc)
print("Sample mean: " + str(mean))

# Calc variance
for x in args.sample:
    temp_placeholder = x
    temp_placeholder -= mean
    temp_placeholder = (temp_placeholder**2)
    sum_of_squares += temp_placeholder

variance = (sum_of_squares / (argc - 1))
print("Sample variance: " + str(variance))

# Calc std_deviation
std_dev = math.sqrt(variance)
print("Sample std deviation: " + str(std_dev))
# Margin of Error
if args.margin_of_error:
    print("margin of error feature not added")
# Confidence level
# feature not added









