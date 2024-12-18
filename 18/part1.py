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

@dataclass()
class Node:
    loc: Coord
    steps: int = 0

def in_bounds(loc: Coord):
    if loc.x < 0 or loc.x > SIZE or loc.y < 0 or loc.y > SIZE:
        return False
    return True

end = Coord(SIZE, SIZE)

m = [[False for x in range(SIZE + 1)] for _ in range(SIZE + 1)]
coords = []
for i, line in enumerate(lines):
    x, y = [int(x) for x in line.split(",")]
    coords.append(Coord(x, y))
    if i < CAP:
        m[y][x] = True
m_viz = [["#" if x else "." for x in line] for line in m]

def display(m):
    for line in m:
        print("".join(line))

display(m_viz)

q = collections.deque()
start = Coord(0, 0)
q.append((start, 0))
visited = {start}
while len(q) != 0:
    node, num_steps = q.popleft()
    # print(node, num_steps)
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
        # print(loc, m[loc.x][loc.y])
        # is wall or out of bounds
        if not in_bounds(loc) or m[loc.y][loc.x]:
            continue
        # update neighbors
        if loc not in visited:
            # print(loc, len(q))
            visited.add(loc)
            q.append((loc, num_steps + 1))