path = 'test.txt'
path = 'input.txt'

file = open(path)
lines = [x.strip() for x in file]

a = []
b = []
for line in lines:
	vala, valb = line.split("   ")
	a.append(int(vala))
	b.append(int(valb))

a.sort()
b.sort()

# part 1
ans = []
for i in range(len(a)):
	ans.append(abs(a[i]-b[i]))

print(sum(ans))

# part 2
counts = dict()
for i in b:
	if i not in counts.keys():
		counts[i] = 0
	counts[i] += 1

ans = 0
for i in a:
	if i in counts.keys():
		ans += i * counts[i]

print(ans)
