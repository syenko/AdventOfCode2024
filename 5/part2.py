import re
import collections
from collections import defaultdict
from functools import cmp_to_key

file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]

rules = defaultdict(list)

i = 0
line = lines[i]
while line != "":
    before, after = (int(x) for x in line.split("|"))
    rules[after].append(before)
    i += 1
    line = lines[i]

def passes_rules(nums):
    nums_to_pages = {num: i for i, num in enumerate(nums)}
    for num in nums:
        position = nums_to_pages[num]
        for rule in rules[num]:
            if rule in nums_to_pages and nums_to_pages[rule] > position:
                return False
    return True

# custom comparator using rules
def compare(a, b):
    if a in rules[b]:
        return -1
    elif b in rules[a]:
        return 1
    else:
        return 0

ans = 0
for line in lines[i + 1:]:
    nums = [int(x) for x in line.split(",")]

    if not passes_rules(nums):
        # sort based on custom comparator
        nums = sorted(nums, key=cmp_to_key(compare))
        ans += nums[len(nums) // 2]

print(ans)