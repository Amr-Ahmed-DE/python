#!/usr/bin/python3

#Task3: print the calendar of a given month and year.

import calendar

year = int(input("Input the year:"))
month = int(input("Input the month:"))

print(calendar.month(year,month, w = 1, l = 0))