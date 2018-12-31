num = input()
for i in range(int(num) - 1):
	print(' ', end = '')
print('*')
for i in range(1, int(num) * 2 - 4, 2):
	for j in range(i, i + 5, 2):
		for k in range(int(num) - (j + 1) // 2):
			print(' ', end = '')
		for l in range(j):
			print('^', end = '')
		print('')
for i in range(int(num) - 2):
	for j in range((int(num) + 1) // 2):
		print(' ', end = '')
	for k in range(int(num) - 2):
		print('#', end = '')
	print('')
		
