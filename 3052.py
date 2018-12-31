num = int(input())
for i in range (1, int((num + 1) / 2 + 1)):
	for j in range (1, i * (-1) + int((num + 1) / 2 + 1)):
		print(' ', end = '')
	for k in range(1, i * 2):
		print('*', end = '')
	print('')
for i in range (1, int((num + 1) / 2)):
	for j in range (1, i + 1):
		print(' ', end = '')
	for k in range(1, i * (-2) + num + 1):
		print('*', end = '')
	print('')
