import re
import collections
import time

file = open('input.txt')
WIDTH = 101
HEIGHT = 103

# WIDTH = 11
# HEIGHT = 7
# file = open('test.txt')

lines = [x.strip() for x in file]

grid = [
    [0 for _ in range(WIDTH)] for _ in range(HEIGHT)
]

class Robot:
    def __init__(self, x, y, v_x, v_y):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y

    def step(self):
        grid[self.y][self.x] -= 1
        self.x += self.v_x
        self.y += self.v_y
        self.x %= WIDTH
        self.y %= HEIGHT
        grid[self.y][self.x] += 1

    def step_i(self, i):
        grid[self.y][self.x] -= 1
        self.x += i * self.v_x
        self.y += i * self.v_y
        self.x %= WIDTH
        self.y %= HEIGHT
        grid[self.y][self.x] += 1


robots = []
# set up robots
for line in lines:
    re_line = re.search("p=(-?\\d+),(-?\\d+) v=(-?\\d+),(-?\\d+)", line)
    x = int(re_line.group(1))
    y = int(re_line.group(2))
    v_x = int(re_line.group(3))
    v_y = int(re_line.group(4))

    robots.append(Robot(x, y, v_x, v_y))

seconds = 0
def step():
    for robot in robots:
        robot.step()

    global seconds
    seconds += 1

while True:
    # guess (hope) picture shows up when no robots are on the same square
    while True:
        step()
        win = True
        for x in grid:
            for y in x:
                if y > 1:
                    win = False

        if win:
            break

    for x in grid:
        print("".join([" " if y == 0 else "*" for y in x]))
    print(seconds)
    input()
