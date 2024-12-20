import queue
import re
import collections
from xmlrpc.client import MAXINT
from enum import Enum
from dataclasses import dataclass, field
from typing import Any, Self, Tuple, List, Set

file = open('input.txt')
# file = open('test.txt')

CHEAT_SECS = 2

lines = [x.strip() for x in file]

m = [[x == "#" for x in line] for line in lines]

nodes = dict()
WIDTH = len(lines[0])
HEIGHT = len(m)

Coord = collections.namedtuple('Coord', ['x', 'y'])

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
def dijkstra(m: List[List[bool]], start: Coord, end: Coord) -> List[Node]:
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

best_path = dijkstra(m, start, end)
best_dist = len(best_path)
print(best_dist - 1)

'''
Solution Idea: 
Save time by jumping ahead on the best path.
To find when you can save time, look at all pairs of 
points on the best path and calculate if you can get
from one to another without walls (manhattan distance).

If you can, see if that actually saves time by checking
how much you jump ahead by.
'''
def manhattan_distance(start, end):
    return abs(end.x - start.x) + abs(end.y - start.y)

dist_saved = []

for i, start in enumerate(best_path):
    for j in range(i + 1, len(best_path)):
        end = best_path[j]
        md = manhattan_distance(start.loc, end.loc)
        if md > CHEAT_SECS or (j-i) - md < 100:
            continue
        dist_saved.append((j-i) - md)
    if i % 100 == 0:
        print(".", end="")

print()
print(len(dist_saved))