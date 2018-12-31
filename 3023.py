d = []
Sum = 0
while True:
	s = int(input())
	if s == -1:
		break
	else:
		if s > 30:
			Sum = Sum + s
		d.append(s)
print(d)
d.sort()
print(d)
print(Sum)
