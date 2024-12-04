import re
import collections
import numpy as np

file = open('input.txt')
# file = open('test.txt')

lines = [[y for y in x.strip()] for x in file]

# lines = ["1234","5123", "6512", "7651"]
# lines = ["abc","def","ghi"]
def is_x_mas(i, j):
    cross = lines[i-1][j-1] + lines[i][j] + lines[i+1][j+1]
    cross2 = lines[i + 1][j - 1] + lines[i][j] + lines[i - 1][j + 1]
    return (cross == "MAS" or cross == "SAM") and (cross2 == "MAS" or cross2 == "SAM")

ans = [1 if is_x_mas(i, j) else 0 for i in range(1, len(lines) - 1) for j in range(1, len(lines[0]) - 1)]

print(sum(ans))

