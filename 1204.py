FileName = input()
f1 = open(FileName, 'r')
data = f1.readlines()
data = [i.strip() for i in data]
f1.close()
for i in range(len(data)):
	if i % 2 == 1:
		if int(data[i]) >= 50:
			print(data[i - 1], data[i])
