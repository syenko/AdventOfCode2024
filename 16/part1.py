import queue
import re
import collections
from xmlrpc.client import MAXINT
from enum import Enum
from dataclasses import dataclass, field
from typing import Any, Self, Tuple

file = open('input.txt')
# file = open('test.txt')
# file = open('test2.txt')

class DIR(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

@dataclass(order=True)
class Node:
    loc: Tuple[int, int]=field(compare=False)
    dir: DIR=field(compare=False)
    prev: Self = field(default=None, compare=False)
    # priority = distance
    dist: int = MAXINT

def get_num_turns(cur_dir, end_dir):
    base_turns = abs(cur_dir.value - end_dir.value)
    return min(base_turns, 4-base_turns)

def in_bounds(loc):
    if loc[0] < 0 or loc[0] >= WIDTH or loc[1] < 0 or loc[1] >= HEIGHT:
        return False
    return True

lines = [x.strip() for x in file]

m = [[x != "#" for x in line] for line in lines]

nodes = dict()
WIDTH = len(lines[0])
HEIGHT = len(m)
TURN_TIME = 1000
MOVE_TIME = 1

start = ()
end = ()

# find start + end, set up nodes dict
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "S":
            start = (x, y)
        elif c == "E":
            end = (x, y)
        for d in DIR:
            nodes[(d, (x, y))] = Node(loc = (x, y), dir = d)

# Dijkstra's Algorithm
q = queue.PriorityQueue()
q.put(Node(start, DIR.EAST, dist=0))
visited = {(DIR.EAST, start)}
while q.qsize() != 0:
    node = q.get()
    prio = node.dist

    # found end!
    if node.loc == end:
        break

    neighbors = [
        (DIR.WEST, (node.loc[0] - 1, node.loc[1])),
        (DIR.EAST, (node.loc[0] + 1, node.loc[1])),
        (DIR.SOUTH, (node.loc[0], node.loc[1] + 1)),
        (DIR.NORTH, (node.loc[0], node.loc[1] - 1))
    ]

    for d, loc in neighbors:
        # is wall or out of bounds
        if not m[loc[1]][loc[0]] or not in_bounds(loc):
            continue
        neighbor_node = nodes[(d, loc)]
        # distance is based on turn direction
        dist = TURN_TIME * get_num_turns(node.dir, d) + 1
        # update neighbors
        if (d, loc) not in visited or node.dist + dist < neighbor_node.dist:
            visited.add((d,loc))
            neighbor_node.dist = node.dist + dist
            neighbor_node.prev = node
            q.put(neighbor_node)

print(f"final dist: {node.dist}")