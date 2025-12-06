import os

print("Advent of Code 2025 - Day 6")

switch = True

unprocessed = []
numbers = []
operations = []

with open(os.getcwd() + "\\Day06\\inputDay6.txt", "r") as input:
    for line in input:
        unprocessed = unprocessed + [line[:-1]]
        splitLine = list(filter(lambda x: x != '', line[:-1].split(' ')))
        if(splitLine[0] == '*' or splitLine[0] == '+'):
            operations =  splitLine
        else:
            numbers = numbers + [list(map(int, splitLine))]

sums = []
for i in range(len(numbers[0])):
    runningCount = 0
    if(operations[i] == '*'):
        runningCount = 1
        for j in range(len(numbers)):
            runningCount *= numbers[j][i]
    else:
        for j in range(len(numbers)):
            runningCount += numbers[j][i]
    sums = sums + [runningCount]

print(sum(sums))

print("Advent of Code 2025 - Day 6 Part 2")

sums = []
numbers = []
for i in range(len(unprocessed[0])):
    index = len(unprocessed[0]) - i - 1
    numbers = numbers + [0]
    for j in range(len(unprocessed) - 1):
        if(unprocessed[j][index] != ' '):
            numbers[len(numbers) - 1] = numbers[len(numbers) - 1] * 10 + int(unprocessed[j][index])
    if(unprocessed[len(unprocessed) - 1][index] == '*'):
        runningCount = 1
        for k in range(0, len(numbers)):
            runningCount *= max(numbers[k], 1)
        sums = sums + [runningCount]
        numbers = []
    if(unprocessed[len(unprocessed) - 1][index] == '+'):
        sums = sums + [sum(numbers)]
        numbers = []

print(sum(sums))
