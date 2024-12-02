file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]

ans = 0
for line in lines:
    vals = [int(x) for x in line.split()]
    safe = True
    # not all increasing / decreasing
    if sorted(vals) != vals and sorted(vals, reverse=True) != vals:
        continue
    # gaps are too small or too large
    for i in range(len(vals) - 1):
        diff = vals[i] - vals[i+1]
        if abs(diff) < 1 or abs(diff) > 3:
            safe = False
            break
    if safe:
        ans += 1

print(ans)