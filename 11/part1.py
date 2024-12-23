import re
import collections
import itertools

file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]
stones = [int(x) for x in lines[0].split()]

NUM_BLINKS = 25

for _ in range(NUM_BLINKS):
    num_stones = len(stones)
    for i in range(num_stones):
        stone = stones[i]
        stonestr = str(stone)
        if stone == 0:
            stones[i] = 1
        elif len(stonestr) % 2 == 0:
            val1, val2 = int(stonestr[:len(stonestr) // 2]), int(stonestr[len(stonestr) // 2:])
            stones[i] = val1
            stones.append(val2)
        else:
            stones[i] = stone * 2024

print(len(stones))