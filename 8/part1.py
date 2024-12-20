import itertools
import re
import collections

class Coord(collections.namedtuple('Coord', ['x', 'y'])):
    def __add__(self, other):
        return Coord(**{field: getattr(self, field) + getattr(other, field)
                        for field in self._fields})
    def __sub__(self, other):
        return Coord(**{field: getattr(self, field) - getattr(other, field)
                        for field in self._fields})

file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]
WIDTH = len(lines[0])
HEIGHT = len(lines)

def in_bounds(loc: Coord):
    if loc.x < 0 or loc.x >= WIDTH or loc.y < 0 or loc.y >= HEIGHT:
        return False
    return True

antennas = collections.defaultdict(list)

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char != ".":
            antennas[char].append(Coord(x, y))

locs = set()

for key, val in antennas.items():
    for a, b in itertools.combinations(val, 2):
        diff = b - a
        p1 = a - diff
        p2 = b + diff
        if in_bounds(p1):
            locs.add(p1)
        if in_bounds(p2):
            locs.add(p2)

print(len(locs))