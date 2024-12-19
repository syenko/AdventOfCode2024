import re
import collections
from enum import Enum

file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]

towels = [x.strip() for x in lines[0].split(", ")]

mem = dict()

def is_possible(s):
    if s == "":
        return 1
    elif s in mem:
        return mem[s]
    else:
        found = 0
        for towel in towels:
            if s.startswith(towel):
                found += is_possible(s[len(towel):])
        mem[s] = found
        return found

ans = 0
for line in lines[2:]:
    ans += is_possible(line)

print(ans)