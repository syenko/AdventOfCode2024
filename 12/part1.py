import re
import collections
import itertools
from collections import namedtuple
from typing import Set, Tuple


class Coord(namedtuple('Coord', ['x', 'y'])):
    def __add__(self, other):
        return Coord(**{field: getattr(self, field) + getattr(other, field)
                        for field in self._fields})
    def __sub__(self, other):
        return Coord(**{field: getattr(self, field) - getattr(other, field)
                        for field in self._fields})

file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]
m = [[val for val in line] for line in lines]
WIDTH = len(m[0])
HEIGHT = len(m)

def in_bounds(loc: Coord):
    if loc.x < 0 or loc.x >= WIDTH or loc.y < 0 or loc.y >= HEIGHT:
        return False
    return True

def get_val(m, coord: Coord) -> str:
    return m[coord.y][coord.x]

def calculate_perimeter(coord: Coord):
    val = get_val(m, coord)
    neighbors = [
        Coord(coord.x - 1, coord.y),
        Coord(coord.x + 1, coord.y),
        Coord(coord.x, coord.y + 1),
        Coord(coord.x, coord.y - 1)
    ]
    count = 0
    for neighbor in neighbors:
        if not in_bounds(neighbor) or get_val(m, neighbor) != val:
            count += 1
    return count

costs = []
visited: Set[Coord] = set()

class Cost(namedtuple("cost", ["area", "perimeter"])):
    def __add__(self, other):
        return Cost(**{field: getattr(self, field) + getattr(other, field)
                        for field in self._fields})

def calculate_cost(coord: Coord, visited: Set[Coord]) -> Cost:
    if coord in visited:
        return Cost(0, 0)

    visited.add(coord)
    node_cost = Cost(1, calculate_perimeter(coord))

    neighbors = [
        Coord(coord.x - 1, coord.y),
        Coord(coord.x + 1, coord.y),
        Coord(coord.x, coord.y + 1),
        Coord(coord.x, coord.y - 1)
    ]

    for neighbor in neighbors:
        if neighbor not in visited and in_bounds(neighbor) and get_val(m, neighbor) == get_val(m, coord):
            node_cost += calculate_cost(neighbor, visited)

    return node_cost

for y, row in enumerate(m):
    for x, val in enumerate(row):
        if Coord(x, y) not in visited:
            cost = calculate_cost(Coord(x, y), visited)
            costs.append(cost.area * cost.perimeter)

print(costs)
print(sum(costs))
