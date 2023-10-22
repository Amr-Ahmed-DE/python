#!/usr/bin/python3

#Task1: Write a python program to count a specific number in a given list

lst = [1,5,5,5,2,3,4,5,1,2,3,4,5,6] #list 
count = 0                           #counter
find_Number = int(input("pleasr enter Number to find its occurrence: "))

#Search to find number occurrence
for i in lst:
    if i == find_Number:
        count = count + 1
    elif lst[i] != find_Number:
        continue
    else:
        continue

print(count)

