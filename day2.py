import os
import math
import re

print("Advent of Code 2025 - Day 2")

ranges = []

with open(os.getcwd() + "\\inputDay2.txt", "r") as input:
    for line in input:
        ranges = ranges + line.split(',')

invalidSum = 0
for i in range(len(ranges)):
    ranges[i] = ranges[i].split('-')
    for j in range(int(ranges[i][0]), int(ranges[i][1]) + 1):
        stringified = str(j)
        if(len(stringified) % 2 == 0 and stringified[:len(stringified) // 2] == stringified[len(stringified) // 2:]):
            invalidSum += j

print(invalidSum)

print("Advent of Code 2025 - Day 2 Part 2")

invalidSum = 0
for i in range(len(ranges)):
    for j in range(int(ranges[i][0]), int(ranges[i][1]) + 1):
        stringified = str(j)
        for k in range(1, math.floor(len(stringified) / 2) + 1):
            regex = '(' + stringified[:k] + ')+'
            if(re.fullmatch(regex, stringified)):
                invalidSum += j
                break

print(invalidSum)
