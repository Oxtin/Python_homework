f1 = open('./stores_old.csv', 'r', encoding = 'Big5')
data = f1.readlines()
f1.close()
for i in range(len(data)):
	data[i] = data[i].strip().split(',')
f2 = open('./stores_new.csv', 'w', encoding = 'UTF-8')
for i in range(len(data)):
	for j in range(len(data[i])):
		if j == 0 or j == 3 or j == 5 or j == 6:
			f2.write(data[i][j] + ',')
	f2.write('\n')
f2.close()
f3 = open('./stores_new.csv', 'r', encoding = 'UTF-8')
ndata = f3.readlines()
f3.close()
for i in range(len(ndata)):
	print(ndata[i].strip())
