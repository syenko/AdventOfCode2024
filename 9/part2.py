import heapq
import queue
import re
import collections
import itertools
from dataclasses import dataclass, field
from heapq import heapify

file = open('input.txt')
# file = open('test.txt')

@dataclass(order = True)
class File:
    id: int=field(compare=True)
    index: int=field(compare=False)
    size: int=field(compare = False)

    def checksum(self):
        return sum([self.id * i for i in range(self.index, self.index + self.size)])

@dataclass(order = True)
class Space:
    index: int=field(compare=True)
    size: int=field(compare=False)

lines = [x.strip() for x in file]
line = [int(char) for char in lines[0]]

files = []
spaces = []
cur_space = 0
for i, val in enumerate(line):
    # is file
    if i % 2 == 0:
        files.append(File(i // 2, cur_space, val))
    else:
        spaces.append(Space(cur_space, val))
    cur_space += val
files.reverse()

ans = 0
for file in files:
    found = False
    for space in spaces:
        # moved too far
        if space.index >= file.index:
            break
        # no space
        if file.size > space.size:
            continue
        # found space!
        found = True
        file.index = space.index

        space.size -= file.size
        space.index += file.size
        if space.size == 0:
            spaces.remove(space)

        ans += file.checksum()
        break
    if not found:
        ans += file.checksum()

print(ans)