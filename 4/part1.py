import re
import collections
import numpy as np

file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]

# lines = ["1234","5123", "6512", "7651"]
# lines = ["abc","def","ghi"]

def countXmas(_lines):
    count = 0
    for line in _lines:
        for i in range(len(line) - 3):
            sel = line[i:i+4]
            if sel == "XMAS" or sel == "SAMX":
                count += 1
    return count



def generateDiagonals(lines):
    linesD = []
    for i in range(len(lines)):
        line = ""
        for j in range(len(lines[i])):
            if i + j >= len(lines):
                break
            line += lines[i + j][j]
        if line != "":
            linesD.append(line)

    for j in range(1, len(lines[0])):
        line = ""
        for i in range(len(lines)):
            if i + j >= len(lines[i]):
                break
            line += lines[i][i+j]
        if line != "":
            linesD.append(line)

    for i in range(len(lines)-1, -1, -1):
        line = ""
        for j in range(len(lines[i])):
            if i - j < 0:
                break
            line += lines[i - j][j]
        if line != "":
            linesD.append(line)

    for j in range(len(lines[0])-1,0, -1):
        line = ""
        for i in range(len(lines)):
            if j + i >= len(lines[i]):
                break
            line += lines[len(lines) - 1 -i][j+i]
        if line != "":
            linesD.append(line)

    return linesD

ans = 0
ans += countXmas(lines)
print(ans)
linesT = ["".join([row[i] for row in lines]) for i in range(len(lines[0]))]
ans += countXmas(linesT)

print(ans)
linesD = generateDiagonals(lines)
print(linesD)
ans += countXmas(linesD)

print(ans)