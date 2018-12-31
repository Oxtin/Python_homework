data = [0]
FileName = input()
f1 = open(FileName, 'r')
d = f1.readlines()
f1.close()
for i in range(1, len(d)):
	data.append(d[i].strip().split(','))
	data[i].append(int(data[i][1]) * 0.1 + int(data[i][2]) * 0.25 + int(data[i][3]) * 0.25 + int(data[i][4]) * 0.4)
Sum = 0
Fail = []
for i in range(1, len(d)):
	Sum = Sum + data[i][5]
	if data[i][5]< 60:
		Fail.append(int(data[i][0]))
print("%d"%(Sum /(len(data) - 1)))
Fail.sort()
for i in range(len(Fail) - 1):
	print(Fail[i], end = ' ')
print(Fail[len(Fail) - 1])
