import os

print("Advent of Code 2025 - Day 3")

lines = []

with open(os.getcwd() + "\\Day03\\inputDay3.txt", "r") as input:
    for line in input:
        lines = lines + [line[:-1]]

joltageSum = 0

for i in range(len(lines)):
    
    firstDigit = max(lines[i][:-1])
    secondDigit = max(lines[i][lines[i].index(firstDigit) + 1:])
    joltageSum += int(firstDigit + secondDigit)

print(joltageSum)

print("Advent of Code 2025 - Day 3 Part 2")

joltageSum = 0

for i in range(len(lines)):
    currentLine = lines[i]
    joltageString = ''
    joltageString = joltageString + max(currentLine[:-11])
    currentLine = currentLine[currentLine.index(joltageString[0]) + 1:]
    for j in range(10):
        joltageString = joltageString + max(currentLine[:(-10 + j)])
        currentLine = currentLine[currentLine.index(joltageString[j + 1]) + 1:]

    joltageString = joltageString + max(currentLine)

    joltageSum += int(joltageString)

print(joltageSum)
