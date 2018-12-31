def x (num):
	if num == 1:
		return (1)
	else:
		return (num * (x (num - 1)))

n = int(input())
print (x(n))

