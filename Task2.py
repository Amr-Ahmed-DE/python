#!/usr/bin/python3

#Task2: Write a python program to accepts the radius of a circule
#       from the user and compute the area.

import math
#get the radious from the user
radius = float(input("please enter the raious:"))

#compute the area
area = math.pi * (radius ** 2)
print(f"The area if the circule = {area}")