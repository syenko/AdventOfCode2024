import re
import collections
import itertools
from collections import defaultdict

file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]
stones = [int(x) for x in lines[0].split()]

stone_dict = defaultdict(int, {stone: 1 for stone in stones})

NUM_BLINKS = 75

for _ in range(NUM_BLINKS):
    num_stones = len(stones)
    og = {a:b for a, b in stone_dict.items()}
    for stone, count in og.items():
        if count == 0:
            continue
        stonestr = str(stone)
        stone_dict[stone] -= count
        if stone == 0:
            stone_dict[1] += count
        elif len(stonestr) % 2 == 0:
            val1, val2 = int(stonestr[:len(stonestr) // 2]), int(stonestr[len(stonestr) // 2:])
            stone_dict[val1] += count
            stone_dict[val2] += count
        else:
            stone_dict[stone * 2024] += count

print(sum(stone_dict.values()))