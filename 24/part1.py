import re
import collections
import itertools
from collections import deque
from dataclasses import dataclass
from enum import Enum

file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]

class Operator(Enum):
    AND = 'AND'
    OR = 'OR'
    XOR = 'XOR'

operator_function = {
    Operator.AND: lambda x, y: x & y,
    Operator.OR: lambda x, y: x | y,
    Operator.XOR: lambda x, y: x ^ y,
}

vals = {}

@dataclass()
class Gate:
    in1: str
    in2: str
    out: str
    op: Operator

    def can_perform_op(self):
        return self.in1 in vals and self.in2 in vals

    def perform_operation(self):
        vals[self.out] = operator_function[self.op](vals[self.in1], vals[self.in2])

for i, line in enumerate(lines):
    if len(line) == 0:
        break
    name, val = line.split(': ')
    val = int(val)
    vals[name] = val

gates = deque()

for line in lines[i+1:]:
    parts = line.split()
    gates.append(Gate(parts[0], parts[2], parts[4], Operator(parts[1])))

while len(gates) > 0:
    next_gate: Gate = gates.popleft()
    if next_gate.can_perform_op():
        next_gate.perform_operation()
    else:
        gates.append(next_gate)

z_vals = [x for x in vals.keys() if x[0] == 'z']
z_vals.sort(reverse=True)
bits = "".join([str(vals[x]) for x in z_vals])
ans = int(bits, 2)
print(ans)