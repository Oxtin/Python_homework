def matrixMultiPly(a, b):
	c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
	for i in range(3):
		for j in range(3):
			sum = 0
			for k in range(3):
				sum = sum + ((a[i][k]) * (b[k][j]))
			c[i][j] = sum
	return (c)
a = []
b = []
tmp = []
for i in range(3):
	tmp = input().split()
	tmp = [int(x) for x in tmp]
	a.append(tmp)
for i in range(3):
	tmp = input().split()
	tmp = [int(x) for x in tmp]
	b.append(tmp)
new = matrixMultiPly(a, b)
for i in range(3):
	print(new[i])
