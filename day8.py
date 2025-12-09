import os
import math

def distanceSQ(pt1, pt2):
    return pow(pt2[0] - pt1[0], 2) + pow(pt2[1] - pt1[1], 2) + pow(pt2[2] - pt1[2], 2)

print("Advent of Code 2025 - Day 8")

switch = True

boxCoords = []

with open(os.getcwd() + "\\inputDay8.txt", "r") as input:
    for line in input:
        boxCoords = boxCoords + [list(map(int, line[:-1].split(',')))]

allEdges = []
for i in range(len(boxCoords)):
    for j in range(i + 1, len(boxCoords)):
        x = distanceSQ(boxCoords[i], boxCoords[j])
        allEdges.append([x, i, j])

allEdges = sorted(allEdges, key=lambda z: z[0])

circuits = []
for k in range(1000):
    edge = allEdges[k]
    if(len(list(filter(lambda z: boxCoords[edge[1]] in z and boxCoords[edge[2]] in z, circuits))) == 0):
        connect0 = list(filter(lambda z: boxCoords[edge[1]] in z, circuits))
        connect1 = list(filter(lambda z: boxCoords[edge[2]] in z, circuits))
        if(not len(connect0) > 0 and not len(connect1) > 0):
            circuits.append([boxCoords[edge[1]], boxCoords[edge[2]]])
        elif(not len(connect1) > 0):
            place = circuits.index(connect0[0])
            circuits[place].append(boxCoords[edge[2]])
        elif(not len(connect0) > 0):
            place = circuits.index(connect1[0])
            circuits[place].append(boxCoords[edge[1]])
        else:
            place0 = circuits.index(connect0[0])
            place1 = circuits.index(connect1[0])
            circuits[place0] = circuits[place0] + circuits[place1]
            circuits[place1] = []

lengths = list(map(len, circuits))
lengths.sort()
print(max(lengths[len(lengths) - 1], 1) * max(lengths[len(lengths) - 2], 1) * max(lengths[len(lengths) - 3], 1))

print("Advent of Code 2025 - Day 8 Part 2")

circuits = [[]]
lastEdge1 = []
lastEdge2 = []
i = 0
while(max(list(map(lambda x: len(x), circuits))) < len(boxCoords)):
    edge = allEdges[i]
    if(len(list(filter(lambda z: boxCoords[edge[1]] in z and boxCoords[edge[2]] in z, circuits))) == 0):
        lastEdge1 = boxCoords[edge[1]]
        lastEdge2 = boxCoords[edge[2]]
        connect0 = list(filter(lambda z: lastEdge1 in z, circuits))
        connect1 = list(filter(lambda z: lastEdge2 in z, circuits))
        if(not len(connect0) > 0 and not len(connect1) > 0):
            circuits.append([boxCoords[edge[1]], boxCoords[edge[2]]])
        elif(not len(connect1) > 0):
            place = circuits.index(connect0[0])
            circuits[place].append(boxCoords[edge[2]])
        elif(not len(connect0) > 0):
            place = circuits.index(connect1[0])
            circuits[place].append(boxCoords[edge[1]])
        else:
            place0 = circuits.index(connect0[0])
            place1 = circuits.index(connect1[0])
            circuits[place0] = circuits[place0] + circuits[place1]
            circuits[place1] = []
    i += 1

print(lastEdge1[0] * lastEdge2[0])
