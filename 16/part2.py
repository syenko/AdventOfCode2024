import queue
import re
import collections
from xmlrpc.client import MAXINT
from enum import Enum
from dataclasses import dataclass, field
from typing import Any, Self, Tuple, Set

file = open('input.txt')
# file = open('test.txt')
# file = open('test2.txt')

class DIR(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

@dataclass(unsafe_hash=True, order=True)
class Node:
    loc: Tuple[int, int]=field(compare=False)
    dir: DIR=field(compare=False)
    prev: Set[Self] = field(default_factory=set, compare=False)
    dist: int = MAXINT

    def get_key(self):
        return self.dir, self.loc

def get_num_turns(cur_dir, end_dir):
    base_turns = abs(cur_dir.value - end_dir.value)
    return min(base_turns, 4-base_turns)

def in_bounds(loc):
    if loc[0] < 0 or loc[0] >= WIDTH or loc[1] < 0 or loc[1] >= HEIGHT:
        return False
    return True

lines = [x.strip() for x in file]

q = queue.PriorityQueue()

m_visual = [[v for v in x] for x in lines]
m = [[x != "#" for x in line] for line in lines]
nodes = dict()
WIDTH = len(lines[0])
HEIGHT = len(m)
TURN_TIME = 1000
MOVE_TIME = 1

start = ()
end = ()

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "S":
            start = (x, y)
        elif c == "E":
            end = (x, y)
        for d in DIR:
            nodes[(d, (x, y))] = Node(loc = (x, y), dir = d)

q.put(Node(start, DIR.EAST, dist=0))
visited = {(DIR.EAST, start)}
best_prio = MAXINT
sol_nodes = set()

def traverse_prev(n):
    sol_nodes.add(n.loc)
    m_visual[n.loc[1]][n.loc[0]] = "O"
    if n.loc == start:
        return
    for prev in n.prev:
        traverse_prev(prev)

while q.qsize() != 0:
    node = q.get()
    prio = node.dist

    if not in_bounds(node.loc):
        continue

    if node.loc == end:
        if node.dist > best_prio:
            break
        best_prio = node.dist
        traverse_prev(node)
        print(node.loc)
        print(prio)

    neighbors = [
        (DIR.WEST, (node.loc[0] - 1, node.loc[1])),
        (DIR.EAST, (node.loc[0] + 1, node.loc[1])),
        (DIR.SOUTH, (node.loc[0], node.loc[1] + 1)),
        (DIR.NORTH, (node.loc[0], node.loc[1] - 1))
    ]

    for d, loc in neighbors:
        if not m[loc[1]][loc[0]] or not in_bounds(loc):
            continue
        neighbor_node = nodes[(d, loc)]
        dist = TURN_TIME * get_num_turns(node.dir, d) + 1
        if (d, loc) not in visited or node.dist + dist <= neighbor_node.dist:
            visited.add((d,loc))
            neighbor_node.dist = node.dist + dist
            if node.dist + dist != neighbor_node.dist:
                neighbor_node.prev.clear()
            neighbor_node.prev.add(node)
            q.put(neighbor_node)

print(f"final dist: {node.dist}")

print(len(sol_nodes))
for line in m_visual:
    print("".join(line))