import re
import collections
import itertools

file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]
line = [int(char) for char in lines[0]]

files = [char for i, char in enumerate(line) if i % 2 == 0]

total_size = sum(line)
cur_space = 0
ans = 0
for i, char in enumerate(line):
    if len(files) == 0:
        break

    # is file
    if i % 2 == 0:
        id = i // 2

        while files[id] > 0:
            ans += cur_space * id
            cur_space += 1
            files[id] -= 1
    # is space
    else:
        j = char
        while j > 0:
            if len(files) == 0:
                break
            id = len(files) - 1
            last = files[id]
            if last == 0:
                files.pop(id)
                continue
            ans += cur_space * id
            cur_space += 1
            files[id] -= 1
            j -= 1

print(ans)
print(total_size, cur_space)