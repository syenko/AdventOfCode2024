import re
import collections
from enum import Enum

file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]

towels = lines[0].split(", ")

def is_possible(s):
    if s == "":
        return True
    else:
        found = False
        for towel in towels:
            if s.startswith(towel):
                found = found or is_possible(s[len(towel):])
        return found

ans = 0
for line in lines[2:]:
    ans += 1 if is_possible(line) else 0

print(ans)