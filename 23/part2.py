import re
import collections
import itertools
from collections import defaultdict
from typing import Set, List

file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]

connections = defaultdict(set)
nodes = set()

for line in lines:
    a, b = line.split("-")
    connections[a].add(a)
    connections[b].add(b)
    connections[a].add(b)
    connections[b].add(a)
    nodes.add(a)
    nodes.add(b)

stack = collections.deque()
visited = set()

print(len(nodes))

# for node, neighbors in connections.items():
#     print(node, len(neighbors), sorted(neighbors))

overlap_counts = defaultdict(set)

for a, b in itertools.combinations(nodes, 2):
    overlap = connections[a].intersection(connections[b])
    overlap_counts[len(overlap)].add((a, b))

max_key = sorted(list(overlap_counts.keys()))[0]
best_overlaps = overlap_counts[max_key]

for a, b in best_overlaps:
    pass

for count, pairs in overlap_counts.items():
    print(f"{count}: {len(pairs)}")