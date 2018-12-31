nName = input()
f = open('./stores_old' + nName + '.csv', 'r', encoding = 'big5')
data = f.readlines()
f.close()
for i in range(len(data)):
	data[i] = data[i].strip().split(',')
f2 = open('./stores_new' + nName + '.csv', 'w', encoding = 'utf-8')
for i in range(len(data)):
	for j in range(len(data[i])):
		if j == 0 or j == 3 or j == 5 or j ==6:
			f2.write(data[i][j] + ',')
	f2.write('\n')
f2.close()
f3 = open('./stores_new' + nName + '.csv', 'r', encoding = 'utf-8')
ndata = f3.readlines()
for i in ndata:
	print(i.strip())
f3.close()
