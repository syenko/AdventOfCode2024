import re
import collections

file = open('input.txt')
WIDTH = 101
HEIGHT = 103

# WIDTH = 11
# HEIGHT = 7
# file = open('test.txt')

lines = [x.strip() for x in file]

quad_count = [0, 0, 0, 0]
for line in lines:
    re_line = re.search("p=(-?\\d+),(-?\\d+) v=(-?\\d+),(-?\\d+)", line)
    x = int(re_line.group(1))
    y = int(re_line.group(2))
    v_x = int(re_line.group(3))
    v_y = int(re_line.group(4))

    final_x = (x + 100 * v_x) % WIDTH
    final_y = (y + 100 * v_y) % HEIGHT

    if final_x < WIDTH // 2 and final_y < HEIGHT // 2:
       quad_count[0] += 1
    elif final_x > WIDTH // 2 and final_y < HEIGHT // 2:
        quad_count[1] += 1
    elif final_x < WIDTH // 2 and final_y > HEIGHT // 2:
        quad_count[2] += 1
    elif final_x > WIDTH // 2 and final_y > HEIGHT // 2:
        quad_count[3] += 1

print(quad_count)

ans = 1
for x in quad_count:
    ans *= x

print(ans)