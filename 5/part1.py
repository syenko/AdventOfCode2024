import re
import collections
from collections import defaultdict

file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]

# read in rules
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

# check if they pass all the rules
ans = 0
for line in lines[i + 1:]:
    nums = [int(x) for x in line.split(",")]

    if passes_rules(nums):
       ans += nums[len(nums) // 2]

print(ans)