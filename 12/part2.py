import re
import collections
import itertools
from collections import namedtuple, defaultdict
from dataclasses import dataclass, field
from enum import Enum
from typing import Set, Tuple, List, Self

file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]
m = [[val for val in line] for line in lines]
WIDTH = len(m[0])
HEIGHT = len(m)

class SideDir(Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"

class Coord(namedtuple('Coord', ['x', 'y'])):
    def __add__(self, other):
        return Coord(**{field: getattr(self, field) + getattr(other, field)
                        for field in self._fields})
    def __sub__(self, other):
        return Coord(**{field: getattr(self, field) - getattr(other, field)
                        for field in self._fields})

@dataclass(order=True, unsafe_hash=True)
class Side:
    '''
    Sides are compared by their main_position and start values, hashed by all
    '''

    dir: SideDir = field(compare=False, hash=True)
    main_pos: int = field(compare=True, hash=True) # value along main axis (height if -, depth if |)
    start: int = field(compare=True, hash=True)
    end: int = field(compare=False, hash=True)
    def get_key(self):
        return self.dir.value + "_" + str(self.main_pos)

    def touching(self, other: Self):
        return self.main_pos == other.main_pos and self.dir == other.dir and (self.end == other.start or self.start == other.end)

    def combine(self, others: List[Self]):
        '''
        Assumes self + others forms continuous side and all have same key
        :param others: list of other sides to combine with
        :return: a single side representing the combined sides
        '''
        for other in others:
            if other.get_key() != self.get_key():
                raise Exception("Cannot combine sides with different keys")

        start_vals = [other.start for other in others]
        start_vals.append(self.start)

        end_vals = [other.end for other in others]
        end_vals.append(self.end)

        return Side(self.dir, self.main_pos, min(start_vals), max(end_vals))

def in_bounds(loc: Coord):
    if loc.x < 0 or loc.x >= WIDTH or loc.y < 0 or loc.y >= HEIGHT:
        return False
    return True

def get_val(m, coord: Coord) -> str:
    return m[coord.y][coord.x]

def get_sides(coord: Coord) -> List[Side]:
    val = get_val(m, coord)
    neighbors = [
        (Coord(coord.x - 1, coord.y), Side(SideDir.WEST, coord.x, coord.y, coord.y + 1)), # W |
        (Coord(coord.x + 1, coord.y), Side(SideDir.EAST, coord.x + 1, coord.y, coord.y + 1)), # | E
        (Coord(coord.x, coord.y - 1), Side(SideDir.NORTH, coord.y, coord.x, coord.x + 1)), # N -
        (Coord(coord.x, coord.y + 1), Side(SideDir.SOUTH, coord.y + 1, coord.x, coord.x + 1)) # S _
    ]
    sides = []
    for neighbor, side in neighbors:
        if not in_bounds(neighbor) or get_val(m, neighbor) != val:
            sides.append(side)

    return sides

costs = []
visited: Set[Coord] = set()


def calculate_cost(coord: Coord, visited: Set[Coord]) -> Tuple[int, List[Side]]:
    if coord in visited:
        return 0, []

    visited.add(coord)
    area = 1
    sides = get_sides(coord)

    neighbors = [
        Coord(coord.x - 1, coord.y),
        Coord(coord.x + 1, coord.y),
        Coord(coord.x, coord.y + 1),
        Coord(coord.x, coord.y - 1)
    ]

    for neighbor in neighbors:
        if neighbor not in visited and in_bounds(neighbor) and get_val(m, neighbor) == get_val(m, coord):
            n_area, n_sides = calculate_cost(neighbor, visited)
            area += n_area
            sides += n_sides

    return area, sides

def count_sides(sides: List[Side]) -> int:
    sides_dict = defaultdict(list)
    for side in sides:
        key = side.get_key()
        new_sides = []
        touching_sides = []
        for added_side in sides_dict[key]:
            if side.touching(added_side):
                touching_sides.append(added_side)
            else:
                new_sides.append(added_side)
        sides_dict[key] = new_sides + [side.combine(touching_sides)]

    return sum([len(sides) for sides in sides_dict.values()])

for y, row in enumerate(m):
    for x, val in enumerate(row):
        if Coord(x, y) not in visited:
            area, sides = calculate_cost(Coord(x, y), visited)
            num_sides = count_sides(sides)
            costs.append(area * num_sides)

print(costs)
print(sum(costs))