import re
import collections
from collections import namedtuple
from dataclasses import dataclass

file = open('input.txt')
SIZE = 70
CAP = 1024
# file = open('test.txt')
# SIZE = 6
# CAP = 12

lines = [x.strip() for x in file]

Coord = namedtuple('Coord', ['x', 'y'])

# helper functions!
def in_bounds(loc: Coord):
    if loc.x < 0 or loc.x > SIZE or loc.y < 0 or loc.y > SIZE:
        return False
    return True

def display(m):
    for line in m:
        print("".join(line))

# read in values
m = [[False for x in range(SIZE + 1)] for _ in range(SIZE + 1)]
coords = []
for i, line in enumerate(lines):
    x, y = [int(x) for x in line.split(",")]
    coords.append(Coord(x, y))
    if i < CAP:
        m[y][x] = True

# for visualization purposes
m_viz = [["#" if x else "." for x in line] for line in m]
display(m_viz)

def bfs() -> bool:
    '''
    conducts bfs starting at (0, 0) and ending at (SIZE, SIZE) on map m
    :return: True if can reach end from start, false otherwise
    '''
    q = collections.deque()
    start = Coord(0, 0)
    end = Coord(SIZE, SIZE)
    q.append((start, 0))
    visited = {start}
    while len(q) != 0:
        node, num_steps = q.popleft()
        # found end!
        if node == end:
            return True

        neighbors = [
            Coord(node.x - 1, node.y),
            Coord(node.x + 1, node.y),
            Coord(node.x, node.y + 1),
            Coord(node.x, node.y - 1)
        ]

        for loc in neighbors:
            # is wall or out of bounds
            if not in_bounds(loc) or m[loc.y][loc.x]:
                continue
            # update neighbors
            if loc not in visited:
                visited.add(loc)
                q.append((loc, num_steps + 1))
    return False

# brute force :D
i = CAP
can_bfs = True
while can_bfs:
    m[coords[i].y][coords[i].x] = True
    can_bfs = bfs()
    i += 1
    # progress bar
    if i % 30 == 0:
        print(".", end="")

print()
print(i)
print(coords[i - 1])