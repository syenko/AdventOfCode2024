import collections
from collections import defaultdict
from typing import List

file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]

connections = defaultdict(list)
nodes = set()

for line in lines:
    a, b = line.split("-")
    connections[a].append(b)
    connections[b].append(a)
    nodes.add(a)
    nodes.add(b)

stack = collections.deque()
visited = set()

t_nodes = [node for node in nodes if node[0] == 't']

t_nodes.sort()
t_sets = set()

def dfs(node: str, start: str, depth: int, cur_set: List[str]):
    # depth 2 good
    if depth == 2:
        if start in connections[node]:
            cur_set.sort()
            t_sets.add(tuple(cur_set))
        return
    visited.add(node)

    for neighbor in connections[node]:
        if neighbor not in visited:
            dfs(neighbor, start, depth + 1, cur_set + [neighbor])

for t_node in t_nodes:
    visited.clear()
    dfs(t_node, t_node, 0, [t_node])

print(len(t_sets))