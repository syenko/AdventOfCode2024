import re
import collections

file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]

nums = [1, 2, 3]

'''
recursive helper function to see if a given equation
can be solved by inserting + or * operators

res is the final answer, cur is the sum so far, i
is the index in nums (global variable)
'''
def can_solve_helper(cur, res, i):
    # if we've reached the end -> return whether we got the right value
    if i == len(nums):
        return cur == res
    # if it's too big -> exist immediately
    if cur > res:
        return False
    else:
        # try both options + / *
        return can_solve_helper(cur * nums[i], res, i + 1) or can_solve_helper(cur + nums[i], res, i + 1)


def get_calibration_value(line):
    res, _nums = line.split(": ")
    res = int(res)
    nums.clear()
    nums.extend([int(x) for x in _nums.strip().split()])

    return res if can_solve_helper(nums[0], res, 1) else 0

ans = [get_calibration_value(line) for line in lines]

print(sum(ans))