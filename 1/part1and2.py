import collections

path = 'test.txt'
path = 'input.txt'

file = open(path)
lines = [x.strip() for x in file]

left = []
right = []
for line in lines:
	left_val, right_val = line.split()
	left.append(int(left_val))
	right.append(int(right_val))

left.sort()
right.sort()

# part 1
ans = []
for i in range(len(left)):
	ans.append(abs(left[i] - right[i]))

print(f"part one: {sum(ans)}")

# part 2
counts = collections.Counter(right)

ans = 0
for i in left:
	ans += i * counts[i]

print(f"part two: {ans}")
