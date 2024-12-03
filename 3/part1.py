import re
file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]

ans = 0
for line in lines:
    for match in re.finditer("mul\\((\d+),(\d+)\\)", line):
        ans += int(match.group(1)) * int(match.group(2))

print(ans)
