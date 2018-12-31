file1 = input()
file2 = input()
f1 = open('../app/' + file1, 'r')
data = f1.readlines()[0].split()
f1.close()
f2 = open('../app/' + file2, 'r')
data.extend(f2.readlines()[0].split())
f2.close()
for i in range(len(data)):
	data[i] = int(data[i]);
data.sort()
for i in range(len(data)):
	print(data[i], end = ' ')
print('')
