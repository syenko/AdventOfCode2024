import re
import collections

file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]
a = int(lines[0].split(": ")[1])
b = int(lines[1].split(": ")[1])
c = int(lines[2].split(": ")[1])
combo_ops = [lambda : 0, lambda : 1, lambda : 2, lambda : 3, lambda : a, lambda : b, lambda : c]

output = []
instructions = [int(x) for x in lines[4].split(": ")[1].split(",")]
cur = 0
print(instructions)
while cur < len(instructions) - 1:
    op = instructions[cur]
    lit = instructions[cur+1]
    combo = combo_ops[lit]()
    # adv -> division
    if op == 0:
        a = a // pow(2, combo)
    elif op == 1:
        b = b ^ lit
    elif op == 2:
        b = combo % 8
    elif op == 3:
        if a != 0:
            cur = lit
            continue
    elif op == 4:
        b = b ^ c
    elif op == 5:
        output.append(combo % 8)
    elif op == 6:
        b = a // pow(2, combo)
    elif op == 7:
        c = a // pow(2, combo)

    cur += 2

print(",".join([str(x) for x in output]))
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
