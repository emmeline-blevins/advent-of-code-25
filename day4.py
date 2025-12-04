import os

print("Advent of Code 2025 - Day 4")

lines = []

with open(os.getcwd() + "\\inputDay4.txt", "r") as input:
    for line in input:
        lines = lines + [list(map(int, list(line[:-1])))]

accessibleSum = 0

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if(lines[i][j] == 1):
            if(i == 0):
                if(j == 0 or j == len(lines[i]) - 1):
                    accessibleSum = accessibleSum + 1
                else:
                    rolls = lines[i][j - 1] + lines[i][j + 1] + lines[i + 1][j - 1] + lines[i + 1][j] + lines[i + 1][j + 1]
                    if(rolls < 4):
                        accessibleSum = accessibleSum + 1
            elif(i == len(lines) - 1):
                if(j == 0 or j == len(lines[i]) - 1):
                    accessibleSum = accessibleSum + 1
                else:
                    rolls = lines[i][j - 1] + lines[i][j + 1] + lines[i - 1][j - 1] + lines[i - 1][j] + lines[i - 1][j + 1]
                    if(rolls < 4):
                        accessibleSum = accessibleSum + 1
            else:
                if(j == 0):
                    rolls = lines[i + 1][j] + lines[i - 1][j] + lines[i + 1][j + 1] + lines[i][j + 1] + lines[i - 1][j + 1]
                    if(rolls < 4):
                        accessibleSum = accessibleSum + 1
                elif(j == len(lines[i]) - 1):
                    rolls = lines[i + 1][j] + lines[i - 1][j] + lines[i + 1][j - 1] + lines[i][j - 1] + lines[i - 1][j - 1]
                    if(rolls < 4):
                        accessibleSum = accessibleSum + 1
                else:     
                    rolls = lines[i - 1][j - 1] + lines[i - 1][j] + lines[i - 1][j + 1] + lines[i][j - 1] + lines[i][j + 1] + lines[i + 1][j - 1] + lines[i + 1][j] + lines[i + 1][j + 1]        
                    if(rolls < 4):
                        accessibleSum = accessibleSum + 1

print(accessibleSum)

print("Advent of Code 2025 - Day 4 Part 2")

totalAccessibleSum = 0
while(accessibleSum > 0):
    accessibleSum = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if(lines[i][j] == 1):
                if(i == 0):
                    if(j == 0 or j == len(lines[i]) - 1):
                        accessibleSum = accessibleSum + 1
                        lines[i][j] = 0
                    else:
                        rolls = lines[i][j - 1] + lines[i][j + 1] + lines[i + 1][j - 1] + lines[i + 1][j] + lines[i + 1][j + 1]
                        if(rolls < 4):
                            accessibleSum = accessibleSum + 1
                            lines[i][j] = 0
                elif(i == len(lines) - 1):
                    if(j == 0 or j == len(lines[i]) - 1):
                        accessibleSum = accessibleSum + 1
                        lines[i][j] = 0
                    else:
                        rolls = lines[i][j - 1] + lines[i][j + 1] + lines[i - 1][j - 1] + lines[i - 1][j] + lines[i - 1][j + 1]
                        if(rolls < 4):
                            accessibleSum = accessibleSum + 1
                            lines[i][j] = 0
                else:
                    if(j == 0):
                        rolls = lines[i + 1][j] + lines[i - 1][j] + lines[i + 1][j + 1] + lines[i][j + 1] + lines[i - 1][j + 1]
                        if(rolls < 4):
                            accessibleSum = accessibleSum + 1
                            lines[i][j] = 0
                    elif(j == len(lines[i]) - 1):
                        rolls = lines[i + 1][j] + lines[i - 1][j] + lines[i + 1][j - 1] + lines[i][j - 1] + lines[i - 1][j - 1]
                        if(rolls < 4):
                            accessibleSum = accessibleSum + 1
                            lines[i][j] = 0
                    else:     
                        rolls = lines[i - 1][j - 1] + lines[i - 1][j] + lines[i - 1][j + 1] + lines[i][j - 1] + lines[i][j + 1] + lines[i + 1][j - 1] + lines[i + 1][j] + lines[i + 1][j + 1]        
                        if(rolls < 4):
                            accessibleSum = accessibleSum + 1
                            lines[i][j] = 0
    totalAccessibleSum += accessibleSum

print(totalAccessibleSum)
