import re
import collections
import itertools

file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]

HEIGHT = 7
WIDTH = 5

locks = []
keys = []

for i in range(0, len(lines), HEIGHT + 1):
    pattern = [sum([1 if lines[j][k] == "#" else 0 for j in range(i, i + HEIGHT)]) for k in range(WIDTH)]

    # lock
    if lines[i] == "#" * WIDTH:
        locks.append(pattern)
    # key
    else:
        keys.append(pattern)

ans = 0
for key in keys:
    for lock in locks:
        ok = all([key[i] + lock[i] <= HEIGHT for i in range(WIDTH)])
        if ok:
            ans += 1

print(ans)