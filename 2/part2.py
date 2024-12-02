file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]

ans = 0
for line in lines:
    vals = [int(x) for x in line.split()]
    safe = True
    print("---")
    print(vals)
    diff = 0
    pos = 0
    for i in range(len(vals) - 1):
        diff_temp = vals[i] - vals[i+1]
        if diff_temp > 0:
            pos += 1
        print(diff_temp)
        diff = diff_temp
        if abs(diff_temp) < 1 or abs(diff_temp) > 3:
            if 0 < i < len(vals) - 1:
                diff_temp = vals[i - 1] - vals[i + 1]
                if abs(diff_temp) < 1 or abs(diff_temp) > 3:
                    print("bad gap")
                    safe = False
                    break
    safe = safe and (pos <= 1 or (len(vals) - 1 - pos) <= 1)
    if not (pos <= 1 or (len(vals) - 1 - pos) <= 1):
        print(pos, "bad")
    if safe:
        ans += 1

print(ans)