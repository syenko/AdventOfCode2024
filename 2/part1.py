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
    if sorted(vals) != vals and sorted(vals, reverse=True) != vals:
        safe = False
    else:
        for i in range(len(vals) - 1):
            diff_temp = vals[i] - vals[i+1]
            print(diff_temp)
            diff = diff_temp
            if abs(diff_temp) < 1 or abs(diff_temp) > 3:
                print("bad gap")
                safe = False
                break
    if safe:
        ans += 1

print(ans)