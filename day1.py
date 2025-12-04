import os
print("Advent of Code 2025 - Day 1")

rotations = []

with open(os.getcwd() + "\\inputDay1.txt", "r") as input:
    for line in input:
        rotations = rotations + [[line[0], int(line[1:-1])]]

position = 50
positions = [position]

for i in range(len(rotations)):
    if(rotations[i][0] == 'L'):
        position = (position - rotations[i][1]) % 100
    elif (rotations[i][0] == 'R'):
        position = (position + rotations[i][1]) % 100
    positions = positions + [position]

zeroes = filter(lambda a: a == 0, positions)

print(len(list(zeroes)))

print("\nAdvent of Code 2025 - Day 1 Part 2")

incrementalRotations = 0
position = 50
for i in range(len(rotations)):
    if(rotations[i][0] == 'L'):
        for j in range(rotations[i][1]):
            position = (position - 1) % 100
            if(position == 0):
                incrementalRotations += 1
    elif (rotations[i][0] == 'R'):
        for j in range(rotations[i][1]):
            position = (position + 1) % 100
            if(position == 0):
                incrementalRotations += 1

print(incrementalRotations)
