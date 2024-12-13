import math
import re
import collections
from xmlrpc.client import MAXINT

import numpy as np

file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]

tokens = 0

A_TOKENS = 3
B_TOKENS = 1

DEBUG = False

def dprint(x):
    if DEBUG:
        print(x)

def is_int(num):
    dprint(f"{num}, {math.isclose(round(num), num)}, {round(num) == num}")
    return math.isclose(round(num), num)

def get_num_tokens(num_a, a, b, sol):
    b_div = np.divide(np.subtract(sol, num_a * a), b)

    if b_div[0] == b_div[1]:
        num_b = b[0]
    else:
        return -1

    if not is_int(num_b) or num_b < 0:
        return -1

    return A_TOKENS * num_a + B_TOKENS * num_b

i = 0
while i < len(lines):
    a_re = re.search("X\\+(\\d+), Y\\+(\\d+)", lines[i])
    ax = int(a_re.group(1))
    ay = int(a_re.group(2))
    i += 1

    b_re = re.search("X\\+(\\d+), Y\\+(\\d+)", lines[i])
    bx = int(b_re.group(1))
    by = int(b_re.group(2))
    i += 1

    p_re = re.search("X=(\\d+), Y=(\\d+)", lines[i])
    px = int(p_re.group(1))
    py = int(p_re.group(2))
    i += 2

    v = np.array([[int(ax), int(bx)], [int(ay), int(by)]])
    sol = np.array([[px], [py]])
    a = np.array([[ax], [by]])
    b = np.array([[ax], [by]])

    if math.isclose((ax / bx),(ay / by)):
        dprint("linear combination!")
        ratio = ax / bx
        if ratio < A_TOKENS / B_TOKENS:
            min_tokens = MAXINT
            max_a = np.max(np.divide(sol, a))
            for i in range(max_a):
                t = get_num_tokens(i, a, b, sol)
                if t != -1:
                    min_tokens = min(t, min_tokens)
            if min_tokens != MAXINT:
                tokens += min_tokens
            else:
                dprint("impossible!")
    else:
        v_inv = np.linalg.inv(v)
        ans = np.matmul(v_inv, sol)
        if not is_int(ans[0][0]) or not is_int(ans[1][0]):
            dprint("not possible (non integer)")
            continue
        else:
            tokens += ans[0] * A_TOKENS + ans[1] * B_TOKENS

print(tokens[0])