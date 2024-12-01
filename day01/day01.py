#!/usr/bin/env python3
import re

list1 = []
list2 = []

with open("./day01/day01-input.txt") as f:
    tuples = re.findall(r"(\d+)\s+(\d+)", f.read())

for singleTuple in tuples:
    list1.append(int(singleTuple[0]))
    list2.append(int(singleTuple[1]))

list1.sort()
list2.sort()

if len(list1) != len(list2):
    raise Exception("help")

def countInList(number, currentList):
    count = 0
    for entry in currentList:
        if number == entry:
            count += 1
    return count

totalDistance = 0
similarityScore = 0

for i in range(len(list1)):
    totalDistance += abs(list1[i] - list2[i])
    similarityScore += list1[i] * countInList(list1[i], list2)

print(f'total distance: {totalDistance}')
print(f'similarity score: {similarityScore}')

