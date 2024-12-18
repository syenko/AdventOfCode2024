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

Coord = namedtuple('Coord', ['x', 'y'])

# helper functions!
def in_bounds(loc: Coord):
    if loc.x < 0 or loc.x > SIZE or loc.y < 0 or loc.y > SIZE:
        return False
    return True

def display(m):
    for line in m:
        print("".join(line))

lines = [x.strip() for x in file]
m = [[False for _ in range(SIZE + 1)] for _ in range(SIZE + 1)]
coords = []
# read in coords
for i, line in enumerate(lines):
    x, y = [int(x) for x in line.split(",")]
    coords.append(Coord(x, y))
    if i < CAP:
        m[y][x] = True

# map for visualization purposes
m_viz = [["#" if x else "." for x in line] for line in m]
display(m_viz)

start = Coord(0, 0)
end = Coord(SIZE, SIZE)

# bfs
q = collections.deque()
q.append((start, 0))
visited = {start}
while len(q) != 0:
    node, num_steps = q.popleft()
    # found end!
    if node == end:
        print(node, num_steps)
        break

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