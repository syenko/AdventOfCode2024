import re
import collections
import itertools
from typing import List

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
m = [[int(val) for val in line] for line in lines]
WIDTH = len(m[0])
HEIGHT = len(m)

def in_bounds(loc: Coord):
    if loc.x < 0 or loc.x >= WIDTH or loc.y < 0 or loc.y >= HEIGHT:
        return False
    return True

visited = set()

def nines_count(coord: Coord, m: List[List[int]]) -> int:
    visited.add(coord)
    height = m[coord.y][coord.x]
    if height == 9:
        return 1
    else:
        neighbors = [
            Coord(coord.x - 1, coord.y),
            Coord(coord.x + 1, coord.y),
            Coord(coord.x, coord.y + 1),
            Coord(coord.x, coord.y - 1)
        ]
        num_nines = 0
        for n in neighbors:
            if n not in visited and in_bounds(n) and m[n.y][n.x] == height + 1:
                num_nines += nines_count(n, m)
        return num_nines

trail_vals = []
for y, line in enumerate(m):
    for x, height in enumerate(line):
        if height == 0:
            visited = set()
            trail_vals.append(nines_count(Coord(x, y), m))

print(sum(trail_vals))