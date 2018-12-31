f1 = open('./stores_old.csv', 'r', encoding = 'Big5')
data = f1.readlines()
f1.close()
for i in range(len(data)):
	data[i] = data[i].strip().split(',')
	for j in range(len(data[i])):
		if j == 0 or j == 3 or j == 5 or j == 6:
			print(data[i][j] + ',', end = '')
	print('')
