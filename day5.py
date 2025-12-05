import os

print("Advent of Code 2025 - Day 5")

valid = []
ids = []

switch = True

with open(os.getcwd() + "\\inputDay5.txt", "r") as input:
    for line in input:
        if(line == '\n'):
            switch = False
        else:
            if(switch):
                startEnd = list(map(int, list(line[:-1].split('-'))))
                valid = valid + [[min(startEnd), max(startEnd)]]
            else:
                ids = ids + [int(line[:-1])]

valid.sort()

notExpired = 0
for id in ids:
    for v in valid:
        if(id >= v[0] and id <= v[1]):
            notExpired += 1
            break

print(notExpired)


allCondensedRanges = valid
timesExpanded = 1
while(timesExpanded > 0):
    timesExpanded = 0
    condensedRanges = []
    for v in allCondensedRanges:
        expanded = False
        for i in range(len(condensedRanges)):
            if(condensedRanges[i][0] <= v[0] and v[0] <= condensedRanges[i][1]):
                condensedRanges[i][1] = max(condensedRanges[i][1], v[1])
                expanded = True
                timesExpanded += 1
            if(condensedRanges[i][0] <= v[1] and v[1] <= condensedRanges[i][1]):
                condensedRanges[i][0] = min(condensedRanges[i][0], v[0])
                expanded = True
                timesExpanded += 1
        if(not expanded):
            condensedRanges = condensedRanges + [[min(v), max(v)]]
    allCondensedRanges[:] = condensedRanges

count = 0
for cr in allCondensedRanges:
    count += cr[1] - cr[0] + 1

print(count)
