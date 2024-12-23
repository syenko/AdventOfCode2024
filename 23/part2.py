import itertools
from collections import defaultdict

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

num_edges = len(connections[a])

def is_fully_connected(nodes):
    for a, b in itertools.combinations(nodes, 2):
        # print(a, b)
        # print(b not in connections[a])
        if b not in connections[a] or a not in connections[b]:
            return False
    return True

for i in range(num_edges):
    found = False
    found_set = set()
    for node, adj in connections.items():
        for node_set in itertools.combinations(adj, num_edges - i):
            if is_fully_connected(node_set):
                found_set = node_set
                found = True
                break
    if found:
        print(",".join(sorted(found_set)))
        break