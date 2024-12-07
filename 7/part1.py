import re
import collections

file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]

nums = [1, 2, 3]

def helper(cur, res, i):
    if i == len(nums):
        return cur == res
    if cur > res:
        return False
    else:
        return helper(cur * nums[i], res, i + 1) or helper(cur + nums[i], res, i + 1)


def is_true(line):
    res, _nums = line.split(": ")
    res = int(res)
    nums.clear()
    nums.extend([int(x) for x in _nums.strip().split()])

    return res if helper(nums[0], res, 1) else 0

ans = [is_true(line) for line in lines]

print(sum(ans))