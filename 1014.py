num = input()
n = 0
for i in range(1,int(num) + 1):
	if i == (int(num)):
		print(str(i), end= '')
	else:
		print(str(i) + '+', end='')
	n = n + int(i)
print(' = ' + str(n))

