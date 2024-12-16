import re
import collections
from collections import namedtuple
from enum import Enum

file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]
WIDTH = len(lines[0])
HEIGHT = len(lines)

Coord = namedtuple("Coord", ["x", "y"])

class DIR(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

global m
m = [[x == "#" for x in line] for line in lines]

guard_start: Coord
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "^":
            guard_start = Coord(x, y)
            break

def in_bounds(loc: Coord) -> bool:
    return 0 <= loc.x < WIDTH and 0 <= loc.y < HEIGHT

def turn(d: DIR) -> DIR:
    return DIR((d.value + 1) % 4)

def loops(x, y) -> bool:
    m[y][x] = True
    guard = guard_start
    visited = set()
    facing = DIR.NORTH
    while in_bounds(guard):
        if (facing, guard) in visited:
            m[y][x] = False
            return True
        visited.add((facing, guard))
        next_space = guard
        if facing == DIR.NORTH:
            next_space = Coord(guard.x, guard.y - 1)
        elif facing == DIR.EAST:
            next_space = Coord(guard.x + 1, guard.y)
        elif facing == DIR.SOUTH:
            next_space = Coord(guard.x, guard.y + 1)
        elif facing == DIR.WEST:
            next_space = Coord(guard.x - 1, guard.y)

        if in_bounds(next_space) and m[next_space.y][next_space.x]:
            facing = turn(facing)
        else:
            guard = next_space

    m[y][x] = False
    return False

def print_arr(m):
    for line in m:
        print("".join(["#" if x else "." for x in line]))

ans = 0
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char != "#":
            print(f"Checking ({x}, {y})")
            ans += 1 if loops(x, y) else 0

print(f"Possible blockers: {ans}")