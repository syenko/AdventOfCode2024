import queue
import re
import collections
from xmlrpc.client import MAXINT
from enum import Enum
from dataclasses import dataclass, field
from typing import Any, Self, Tuple, List, Set

file = open('input.txt')
# file = open('test.txt')

Coord = collections.namedtuple('Coord', ['x', 'y'])

CHEAT_SECS = 20

lines = [x.strip() for x in file]

m = [[x == "#" for x in line] for line in lines]
# map for visualization purposes
m_visual = [[v for v in x] for x in lines]

nodes = dict()
WIDTH = len(lines[0])
HEIGHT = len(m)
TURN_TIME = 1000
MOVE_TIME = 1

@dataclass(unsafe_hash=True, order=True)
class Node:
    loc: Coord=field(compare=False, hash=True)
    prev: Self = field(default=None, compare=False, hash=False)
    dist: int = field(default=MAXINT, hash=False)

def in_bounds(loc: Coord):
    if loc.x < 0 or loc.x >= WIDTH or loc.y < 0 or loc.y >= HEIGHT:
        return False
    return True

start = ()
end = ()

# find start + end, set up nodes dict
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "S":
            start = Coord(x, y)
        elif c == "E":
            end = Coord(x, y)
        nodes[Coord(x, y)] = Node(loc = Coord(x, y))

# Dijkstra's Algorithm
def dijkstra_norm(m, start, end):
    q = queue.PriorityQueue()
    q.put(Node(start, 0, dist=0))
    visited = {(0, start)}
    while q.qsize() != 0:
        node: Node = q.get()
        prio = node.dist

        # found end!
        if node.loc == end:
            cur = node
            ans = []
            while cur.loc != start:
                ans.insert(0, cur)
                cur = cur.prev
            ans.insert(0, cur)
            return ans

        neighbors = [
            Coord(node.loc.x - 1, node.loc.y),
            Coord(node.loc.x + 1, node.loc.y),
            Coord(node.loc.x, node.loc.y + 1),
            Coord(node.loc.x, node.loc.y - 1)
        ]

        for loc in neighbors:
            # out of bounds or wall if already cheated
            if not in_bounds(loc) or m[loc.y][loc.x]:
                continue
            neighbor_node = nodes[loc]
            # update neighbors
            if loc not in visited or node.dist + 1 < neighbor_node.dist:
                visited.add(loc)
                neighbor_node.dist = node.dist + 1
                neighbor_node.prev = node
                q.put(neighbor_node)

best_path = dijkstra_norm(m, start, end)
best_dist = len(best_path)
print(best_dist - 1)

def manhatten_distance(start, end):
    return abs(end.x - start.x) + abs(end.y - start.y)

dist_saved = []

for i, start in enumerate(best_path):
    for j in range(i + 1, len(best_path)):
        end = best_path[j]
        # too far
        md = manhatten_distance(start.loc, end.loc)
        if md > CHEAT_SECS or (j-i) - md < 100:
            continue
        dist_saved.append((j-i) - md)

print(dist_saved)
print(len(dist_saved))