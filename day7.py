import os

print("Advent of Code 2025 - Day 7")

switch = True

lines = []

with open(os.getcwd() + "\\inputDay7.txt", "r") as input:
    for line in input:
        lines = lines + [line[:-1]]

activeBeams = []
splitCt = 0

for i in range(0, len(lines), 1):
    prevBeams = list(activeBeams)
    activeBeams = []
    for j in range(len(lines[i])):
        if(lines[i][j] == 'S'):
            activeBeams = [j]
        elif(lines[i][j] == '^'):
            if(j in prevBeams):
                splitCt += 1
                if(j > 0):
                    activeBeams = activeBeams + [j - 1]
                if(j < len(lines[i]) - 1):
                    activeBeams = activeBeams + [j + 1]
        elif(j in prevBeams):
            activeBeams = activeBeams + [j]

print(splitCt)

activeBeams = []
activeTimelines = []
for i in range(0, len(lines), 2):
    prevBeams = list(activeBeams)
    prevTimelines = list(activeTimelines)
    activeBeams = []
    activeTimelines = []
    for j in range(len(lines[i])):
        if(lines[i][j] == 'S'):
            activeBeams = [j]
            activeTimelines = [(j, 1)]
        elif(lines[i][j] == '^'):
            if(j in prevBeams):
                if(j > 0):
                    if(j - 1 not in activeBeams):
                        activeBeams = activeBeams + [j - 1]
                    activeTimelines = activeTimelines + [(j - 1, sum(map(lambda z: z[1], filter(lambda x: x[0] == j, prevTimelines))))]
                if(j < len(lines[i]) - 1):
                    if(j + 1 not in activeBeams):
                        activeBeams = activeBeams + [j + 1]
                    activeTimelines = activeTimelines + [(j + 1, sum(map(lambda z: z[1], filter(lambda x: x[0] == j, prevTimelines))))]
                    
        elif(j in prevBeams):
            activeBeams = activeBeams + [j]
            activeTimelines = activeTimelines + [(j, sum(map(lambda z: z[1], filter(lambda x: x[0] == j, prevTimelines))))]

print(activeTimelines)
print(sum(map(lambda z: z[1],activeTimelines)))
