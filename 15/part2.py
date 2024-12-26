import collections
from dataclasses import dataclass
from typing import Any, Self

file = open('input.txt')
# file = open('test.txt')

class Coord(collections.namedtuple('Coord', ['x', 'y'])):
    def __add__(self, other):
        return Coord(**{field: getattr(self, field) + getattr(other, field)
                        for field in self._fields})
    def __sub__(self, other):
        return Coord(**{field: getattr(self, field) - getattr(other, field)
                        for field in self._fields})

def get_val(m, coord: Coord) -> Any:
    return m[coord.y][coord.x]

def set_val(m, coord: Coord, val):
    m[coord.y][coord.x] = val

move_to_get_next = {
    "<": lambda coord: Coord(coord.x - 1, coord.y),
    ">": lambda coord: Coord(coord.x + 1, coord.y),
    "v": lambda coord: Coord(coord.x, coord.y + 1),
    "^": lambda coord: Coord(coord.x, coord.y - 1)
}

@dataclass()
class Box:
    left_loc: Coord
    right_loc: Coord
    index: int

    def get_new_box(self, command: str) -> Self:
        f = move_to_get_next[command]
        return Box(f(self.left_loc), f(self.right_loc), self.index)

lines = [x.strip() for x in file]

split_index = 0
while lines[split_index] != "":
    split_index += 1

# true if wall, false if not
m = [[x for char in line for x in ["#" if char == "#" else "."] * 2] for line in lines[:split_index]]

boxes = []
start = None
for y, line in enumerate(lines[:split_index]):
    for x, char in enumerate(line):
        # box
        if char == "O":
            index = len(boxes)
            new_box = Box(Coord(2 * x, y), Coord(2 * x + 1, y), index)
            set_val(m, new_box.left_loc, index)
            set_val(m, new_box.right_loc, index)
            boxes.append(new_box)

        elif char == "@":
            start = Coord(2 * x, y)

WIDTH = len(m[0])
HEIGHT = len(m)

def in_bounds(loc: Coord):
    if loc.x < 0 or loc.x >= WIDTH or loc.y < 0 or loc.y >= HEIGHT:
        return False
    return True

def get_val(m, coord: Coord) -> str:
    return m[coord.y][coord.x]

commands = []
for line in lines[split_index+1:]:
    commands += [char for char in line]

def try_move(coord: Coord, direction: str):
    val = get_val(m, coord)
    # is wall
    if val == "#":
        return False

    # is space
    if val == ".":
        return True

    # is box
    box = boxes[val]
    new_box = box.get_new_box(direction)

    if direction == "<":
        can_move = try_move(new_box.left_loc, direction)
    elif direction == ">":
        can_move = try_move(new_box.right_loc, direction)
    else:
        can_move = try_move(new_box.left_loc, direction) and try_move(new_box.right_loc, direction)

    return can_move

def update(coord: Coord, direction: str):
    val = get_val(m, coord)
    # is not box
    if val == "#" or val == ".":
        return

    # is box
    box = boxes[val]
    new_box = box.get_new_box(direction)

    if direction == "<":
        update(new_box.left_loc, direction)
    elif direction == ">":
        update(new_box.right_loc, direction)
    else:
        update(new_box.left_loc, direction)
        update(new_box.right_loc, direction)

    # move box
    set_val(m, box.left_loc, ".")
    set_val(m, box.right_loc, ".")
    set_val(m, new_box.left_loc, new_box.index)
    set_val(m, new_box.right_loc, new_box.index)
    boxes[new_box.index] = new_box

def print_map():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            val = get_val(m, Coord(x, y))
            if Coord(x, y) == start:
                print("@", end="")
            elif val == "#":
                print("#", end="")
            elif val == ".":
                print(".", end="")
            else:
                print("O", end="")
        print("")

for command in commands:
    next_loc = move_to_get_next[command](start)
    can_move = try_move(next_loc, command)
    if can_move:
        update(next_loc, command)
        start = next_loc
    # print_map()
print(sum([box.left_loc.x + 100 * box.left_loc.y for box in boxes]))