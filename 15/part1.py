import collections
from dataclasses import dataclass

file = open('input.txt')
# file = open('test.txt')

class Coord(collections.namedtuple('Coord', ['x', 'y'])):
    def __add__(self, other):
        return Coord(**{field: getattr(self, field) + getattr(other, field)
                        for field in self._fields})
    def __sub__(self, other):
        return Coord(**{field: getattr(self, field) - getattr(other, field)
                        for field in self._fields})

move_to_get_next = {
    "<": lambda coord: Coord(coord.x - 1, coord.y),
    ">": lambda coord: Coord(coord.x + 1, coord.y),
    "v": lambda coord: Coord(coord.x, coord.y + 1),
    "^": lambda coord: Coord(coord.x, coord.y - 1)
}

lines = [x.strip() for x in file]

split_index = 0
while lines[split_index] != "":
    split_index += 1

# true if wall, false if not
m = [[char == "#" for char in line] for line in lines[:split_index]]

boxes = set()
start = None
for y, line in enumerate(lines[:split_index]):
    for x, char in enumerate(line):
        # box
        if char == "O":
            boxes.add(Coord(x, y))
        elif char == "@":
            start = Coord(x, y)

WIDTH = len(m[0])
HEIGHT = len(m)

def get_val(m, coord: Coord) -> str:
    return m[coord.y][coord.x]

commands = []
for line in lines[split_index+1:]:
    commands += [char for char in line]

def move(coord: Coord, direction: str):
    # is wall
    if get_val(m, coord):
        return False

    # is space
    if coord not in boxes:
        return True

    # is box
    next_loc = move_to_get_next[direction](coord)

    can_move = move(next_loc, direction)

    if can_move:
        boxes.remove(coord)
        boxes.add(next_loc)

    return can_move

def print_map():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if Coord(x, y) in boxes:
                print("O", end="")
            elif get_val(m, Coord(x, y)):
                print("#", end="")
            elif Coord(x, y) == start:
                print("@", end="")
            else:
                print(".", end="")
        print("")

for command in commands:
    next_loc = move_to_get_next[command](start)
    can_move = move(next_loc, command)
    if can_move:
        start = next_loc

print(sum([box.x + 100 * box.y for box in boxes]))