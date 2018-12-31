d = []
while True:
	a = int(input())
	if (a == -1):
		break
	else:
		d.append(a)
d.sort()
print(d)
d.insert(3, 10)
print(d)
print(d.count(10))
d.sort()
d.reverse()
print(d)
