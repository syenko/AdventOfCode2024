file = open('input.txt')
# file = open('test.txt')

lines = [x.strip() for x in file]

def is_safe(vals):
    safe = True
    diff = 0
    if sorted(vals) != vals and sorted(vals, reverse=True) != vals:
        safe = False
    else:
        for i in range(len(vals) - 1):
            diff = vals[i] - vals[i + 1]
            if abs(diff) < 1 or abs(diff) > 3:
                safe = False
                break
    return safe

ans = 0
for line in lines:
    vals = [int(x) for x in line.split()]

    safe_vals = [is_safe(vals)]
    for i in range(len(vals)):
        removed = vals.pop(i)
        safe_vals.append(is_safe(vals))
        vals.insert(i, removed)

    safe = any(safe_vals)
    if safe:
        ans += 1

print(ans)