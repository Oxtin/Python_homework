num = int(input())
ind = 1
for i in range(1, num + 1):
	for j in range(ind, ind + i):
		ind = ind + 1
		print(str(j), end = ' ')
	print('')
