import heapq
import queue
import re
import collections
import itertools
from dataclasses import dataclass, field
from heapq import heapify

file = open('input.txt')
# file = open('test.txt')

@dataclass(order = True)
class File:
    priority: int
    id: int=field(compare=False)
    size: int=field(compare = False)

lines = [x.strip() for x in file]
line = [int(char) for char in lines[0]]

files = queue.PriorityQueue()
for i in range(0, len(line), 2):
    files.put(File(-(i // 2), i // 2, line[i]))
file_counted = [False] * files.qsize()

total_size = sum(line)
cur_space = 0
ans = 0
for i, char in enumerate(line):
    if files.qsize() == 0:
        break

    # is file
    if i % 2 == 0 and not file_counted[i // 2]:
        id = i // 2
        file_counted[id] = True

        for _ in range(char):
            ans += cur_space * id
            cur_space += 1
    # is space
    else:
        empty_space = char
        re_add = []
        while empty_space > 0:
            # deque by highest priority until we find one that's the right size
            file: File = files.get()
            not_found = False
            # if q > empty_space then add to re_add if not file_counted
            while file.size > empty_space:
                if not file_counted[file.id]:
                    re_add.append(file)
                # no file fits in the space
                if files.qsize() == 0:
                    not_found = True
                    break
                file = files.get()
            # no file fits in the space -> break and move on
            if not_found:
                cur_space += empty_space
                break
            file_counted[file.id] = True
            # once found -> decrement empty_space, count spaces filled, change file_counted
            empty_space -= file.size
            for _ in range(file.size):
                ans += cur_space * file.id
                cur_space += 1
        # requeue items into queue that were removed
        for item in re_add:
            files.put(item)


print(ans)
print(total_size, cur_space)