import re
file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]

ans = 0
enabled = True
for line in lines:
    for match in re.finditer("(do\\(\\))|(don't\\(\\))|(mul\\((\\d+),(\\d+)\\))", line):
        # do
        if match.group(1):
            enabled = True
        # do not
        elif match.group(2):
            enabled = False
        # multiply
        elif match.group(3):
            if enabled:
                ans += int(match.group(4)) * int(match.group(5))

print(ans)
