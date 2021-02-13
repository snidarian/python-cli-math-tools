#! /usr/local/bin/python3.9
# This program takes any piece of a circle and calculates the other pieces

"""
circumference/diameter = pi = 3.14159
circumference = pi * diameter
diameter = 2 * radius
circumference = 2 * pi * radius
Area = pi * r^2
area = (pi/4)*diameter^2
"""

import math
import argparse

parser = argparse.ArgumentParser(description='CLI tool for calculating circle measurements.')

args = parser.add_argument("-c", "--circumference", help="Circumference measurement", type=float)
args = parser.add_argument("-r", "--radius", help="Radius measurement", type=float)
args = parser.add_argument("-d", "--diameter", help="Diameter measurement", type=float)
args = parser.add_argument("-a", "--area", help="Area measurement", type=float)

args = parser.parse_args()

circumference = 0
radius = 0
diameter = 0
area = 0
pi = 3.14159

if args.circumference:
    circumference = args.circumference
    print("Circumference: " + str(circumference))
    diameter = (circumference / pi)
    print("Diameter: " + str(diameter))
    radius = (diameter / 2)
    print("Radius: " + str(radius))
    area = (pi * (radius**2))
    print("Area: " + str(area))
elif args.radius:
    radius = args.radius
    print("Radius: " + str(radius))
    diameter = (2 * radius)
    print("Diameter: " + str(diameter))
    circumference = (2 * pi * radius)
    print("Circumference: " + str(circumference))
    area = (pi * (radius**2))
    print("Area: " + str(area))
elif args.diameter:
    diameter = args.diameter
    print("Diameter: " + str(diameter))
    radius = (diameter / 2)
    print("Radius: " + str(radius))
    circumference = (pi * diameter)
    print("Circumference: " + str(circumference))
    area = pi * ((diameter/2) ** 2)
    print("Area: " + str(area))
elif args.area:
    area = args.area
    print("Area: " + str(area))
    radius = math.sqrt((area / pi))
    print("Radius: " + str(radius))
    diameter = math.sqrt(((4*area)/pi))
    print("Diameter: " + str(diameter))
    circumference = 2*(math.sqrt((pi*area)))
    print("Circumference: " + str(circumference))
else:
    print("Error: provide valid cli flags and their arguments\nChoose one measurement argument only.")







